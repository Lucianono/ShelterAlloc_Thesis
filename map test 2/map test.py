import osmnx as ox
import folium
import pandas as pd
import time #can be removed after.

# Define a list of colors for the routes
ROUTE_COLORS = ['blue', 'green', 'red', 'purple', 'orange', 'pink', 'yellow', 'brown', 'gray', 'cyan']

def get_route_color(iteration_index):
    return ROUTE_COLORS[iteration_index % len(ROUTE_COLORS)]

def plot_routes_on_map(communities_df, shelters_df, map_name="all_routes_map.html", excel_name="distance_matrix.xlsx"):
    # Center the map at the average location of all communities and shelters
    avg_lat = (communities_df['xDegrees'].mean() + shelters_df['xDegrees'].mean()) / 2
    avg_lon = (communities_df['yDegrees'].mean() + shelters_df['yDegrees'].mean()) / 2
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=13)

    # Add markers for communities using the "Name" column
    for _, community in communities_df.iterrows():
        folium.Marker([community['xDegrees'], community['yDegrees']], popup=f"Community: {community['Name']}",
                      icon=folium.Icon(color='green')).add_to(m)
    
    # Add markers for shelters using the "Name" column
    for _, shelter in shelters_df.iterrows():
        folium.Marker([shelter['xDegrees'], shelter['yDegrees']], popup=f"Shelter: {shelter['Name']}",
                      icon=folium.Icon(color='red')).add_to(m)

    # Create an empty dictionary to store distances
    distance_matrix = {}

    # Plot routes from each community to each shelter with different colors
    route_counter = 0  # Counter to cycle through route colors

    for _, community in communities_df.iterrows():
        community_coords = (community['xDegrees'], community['yDegrees'])
        community_name = community['Name']
        
        # Initialize an empty list for distances for the current community
        distance_matrix[community_name] = []

        for _, shelter in shelters_df.iterrows():
            shelter_coords = (shelter['xDegrees'], shelter['yDegrees'])
            shelter_name = shelter['Name']

            lat1, lon1 = community_coords
            lat2, lon2 = shelter_coords

            # Create the road graph within a larger bounding box defined by the points
            bbox = (lat1 + 0.05, lat2 - 0.05, lon1 + 0.05, lon2 - 0.05)

            roadgraph = ox.graph_from_bbox(*bbox, network_type='drive')

            if roadgraph is None or len(roadgraph.nodes) == 0:
                print(f"Skipping route from Community {community_name} to Shelter {shelter_name}: Empty road graph.")
                continue

            # Find the nearest nodes to the starting and ending points
            start_node = ox.distance.nearest_nodes(roadgraph, lon1, lat1)
            end_node = ox.distance.nearest_nodes(roadgraph, lon2, lat2)

            if start_node is None or end_node is None:
                print(f"Error: Could not find nodes for the route from {community_name} to {shelter_name}.")
                continue

            # Find the shortest path between the nodes
            try:
                route = ox.shortest_path(roadgraph, start_node, end_node)
            except Exception as e:
                print(f"Error: Could not compute shortest path from {community_name} to {shelter_name}. {e}")
                continue
            
            # Calculate the total route distance
            route_distance = sum(ox.utils_graph.get_route_edge_attributes(roadgraph, route, 'length'))
            print(f"Distance from {community_name} to {shelter_name}: {route_distance / 1000:.2f} km")

            # Use the convert module to extract the GeoDataFrame for nodes
            try:
                gdf_nodes, gdf_edges = ox.convert.graph_to_gdfs(roadgraph)
            except Exception as e:
                print(f"Error: Could not convert the graph to GeoDataFrames for {community_name} to {shelter_name}. {e}")
                continue

            # Get the route coordinates from the nodes
            route_coords = []
            for node in route:
                try:
                    # Extract coordinates for each node in the route
                    node_data = gdf_nodes.loc[node]
                    route_coords.append((node_data['y'], node_data['x']))
                except KeyError:
                    print(f"Warning: Node {node} not found in the graph.")
                    continue

            if not route_coords:
                print(f"Error: No valid route coordinates found for {community_name} to {shelter_name}.")
                continue

            # Get the color for this route
            route_color = get_route_color(route_counter)

            # Add polyline to the map
            folium.PolyLine(route_coords, color=route_color, weight=2.5, opacity=0.7,
                            popup=f"Route from Community {community_name} to Shelter {shelter_name}").add_to(m)

            # Store the distance in the matrix
            distance_matrix[community_name].append(route_distance / 1000)  # Convert to km

            # Increment the route counter to change the color for the next route
            route_counter += 1

            # Print the time when the iteration is done
            current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print(f"Done with route from {community_name} to {shelter_name}. Time: {current_time}")

    # Convert the distance dictionary to a pandas DataFrame
    distance_df = pd.DataFrame(distance_matrix, index=[shelter['Name'] for _, shelter in shelters_df.iterrows()])

    # Save the distance matrix to an Excel file
    distance_df.to_excel(excel_name)
    print(f"Distance matrix saved as {excel_name}")

    # Save the map to an HTML file
    m.save(map_name)
    print(f"Map with all routes saved as {map_name}")

    # Return the map object
    return m

# Load data from Excel files
communities_df = pd.read_excel('community-data.xlsx')
shelters_df = pd.read_excel('shelter-data.xlsx')

# Plot all routes on a single map and generate the distance matrix
plot_routes_on_map(communities_df, shelters_df)
