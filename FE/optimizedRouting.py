import osmnx as ox
import folium
import pandas as pd
import time
from math import radians, cos, sin, sqrt, atan2
import networkx as nx

# Define a list of colors for the routes
ROUTE_COLORS = ['blue', 'green', 'red', 'purple', 'orange', 'pink', 'yellow', 'brown', 'gray', 'cyan']

def get_route_color(iteration_index):
    return ROUTE_COLORS[iteration_index % len(ROUTE_COLORS)]

def haversine_distance(lat1, lon1, lat2, lon2):
    # Calculate haversine distance in meters
    R = 6371000  # Earth's radius in meters
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi / 2)**2 + cos(phi1) * cos(phi2) * sin(dlambda / 2)**2
    return 2 * R * atan2(sqrt(a), sqrt(1 - a))

def plot_optimized_routes(communities_df, shelters_df, map_name="optimized-routes-map.html", progress_callback=None):
    # Center the map at the average location of all communities and shelters
    avg_lat = (communities_df['xDegrees'].mean() + shelters_df['xDegrees'].mean()) / 2
    avg_lon = (communities_df['yDegrees'].mean() + shelters_df['yDegrees'].mean()) / 2
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=13)

    # Add markers for communities
    for _, community in communities_df.iterrows():
        folium.Marker([community['xDegrees'], community['yDegrees']], 
                      popup=f"Community: {community['Community Name']}",
                      icon=folium.Icon(color='green')).add_to(m)
    
    # Add markers for shelters
    for _, shelter in shelters_df.iterrows():
        folium.Marker([shelter['xDegrees'], shelter['yDegrees']], 
                      popup=f"Shelter: {shelter['Shelter Assigned']}",
                      icon=folium.Icon(color='red')).add_to(m)

    # Define a bounding box for the entire region
    bbox_margin = 0.02
    bbox = (
        max(communities_df['xDegrees'].max(), shelters_df['xDegrees'].max()) + bbox_margin,
        min(communities_df['xDegrees'].min(), shelters_df['xDegrees'].min()) - bbox_margin,
        max(communities_df['yDegrees'].max(), shelters_df['yDegrees'].max()) + bbox_margin,
        min(communities_df['yDegrees'].min(), shelters_df['yDegrees'].min()) - bbox_margin
    )

    # Load the road graph for the region
    roadgraph = ox.graph_from_bbox(*bbox, network_type='drive')

    # Precompute node coordinates for the heuristic
    node_coords = {node: (data['y'], data['x']) for node, data in roadgraph.nodes(data=True)}

    def haversine_heuristic(u, v):
        lat1, lon1 = node_coords[u]
        lat2, lon2 = node_coords[v]
        return haversine_distance(lat1, lon1, lat2, lon2)

    # Plot routes from each community to each shelter
    route_counter = 0

    for _, community in communities_df.iterrows():
        for _, shelter in shelters_df.iterrows():
            try:

                shelter = shelters_df.loc[communities_df.index == community.name].iloc[0]
                
                # Get the nearest nodes
                start_node = ox.distance.nearest_nodes(roadgraph, community['yDegrees'], community['xDegrees'])
                end_node = ox.distance.nearest_nodes(roadgraph, shelter['yDegrees'], shelter['xDegrees'])

                # Find the shortest path using A* algorithm
                route = nx.astar_path(roadgraph, start_node, end_node, heuristic=haversine_heuristic, weight='length')

                # Calculate the total route distance
                route_distance = sum(ox.utils_graph.get_route_edge_attributes(roadgraph, route, 'length'))

                # Get the route coordinates
                route_coords = [(node_coords[node][0], node_coords[node][1]) for node in route]

                # Add the route to the map
                route_color = get_route_color(route_counter)
                folium.PolyLine(route_coords, color=route_color, weight=2.5, opacity=0.7,
                                popup=f"Route from {community['Community Name']} to {shelter['Shelter Assigned']}").add_to(m)

                # Increment the route counter
                route_counter += 1

                print(f"Route from {community['Community Name']} to {shelter['Shelter Assigned']}: {route_distance / 1000:.2f} km")

            except nx.NetworkXNoPath:
                print(f"No path found from {community['Community Name']} to {shelter['Shelter Assigned']}.")
                continue
            except Exception as e:
                print(f"Error processing route from {community['Community Name']} to {shelter['Shelter Assigned']}: {e}")
                continue

    # Save the map to an HTML file
    m.save(map_name)
    print(f"Map with all routes saved as {map_name}")

    return m

def run_optimization(communities_file='allocation_results.xlsx', shelters_file='allocation_results.xlsx'):
    # Load data from the Excel file
    communities_df = pd.read_excel(communities_file, usecols=["Community Name", "Community Latitude", "Community Longitude"])
    shelters_df = pd.read_excel(shelters_file, usecols=["Shelter Assigned", "Shelter Latitude", "Shelter Longitude"])

    # Rename columns to 'xDegrees' and 'yDegrees' for consistent use across the code
    communities_df.rename(columns={
        'Community Latitude': 'yDegrees', 
        'Community Longitude': 'xDegrees'
    }, inplace=True)
    
    shelters_df.rename(columns={
        'Shelter Latitude': 'yDegrees', 
        'Shelter Longitude': 'xDegrees'
    }, inplace=True)

    # Check that the renaming worked correctly
    print("Communities Dataframe Columns: ", communities_df.columns)
    print("Shelters Dataframe Columns: ", shelters_df.columns)

    # Plot all routes on a single map
    plot_optimized_routes(communities_df, shelters_df)
