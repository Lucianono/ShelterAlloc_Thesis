import osmnx as ox
import folium
from folium.plugins import AntPath
import os
import pandas as pd
import networkx as nx
from math import radians, cos, sin, sqrt, atan2
from folium.plugins import MousePosition

# Define a list of colors for the routes
ROUTE_COLORS = ['darkblue', 'darkgreen', 'darkred', 'indigo', 'darkorange', 'maroon', 
                'darkgoldenrod', 'saddlebrown', 'dimgray', 'teal', 'blue', 'green', 'red', 'purple', 'orange', 'pink', 'yellow', 'brown', 'gray', 'cyan']
save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")

def get_route_color(iteration_index):
    return ROUTE_COLORS[iteration_index % len(ROUTE_COLORS)]

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371000  # Earth's radius in meters
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi / 2)**2 + cos(phi1) * cos(phi2) * sin(dlambda / 2)**2
    return 2 * R * atan2(sqrt(a), sqrt(1 - a))

def plot_optimized_routes(allocation_df, comm_dict, shel_dict, map_name="optimized-routes-map.html"):
    print("Running plot_optimized_routes")

    # Add coordinates using lookup dictionaries
    allocation_df['Latitude_Comm'] = allocation_df['Community'].map(lambda x: comm_dict.get(x, {}).get('x'))
    allocation_df['Longitude_Comm'] = allocation_df['Community'].map(lambda x: comm_dict.get(x, {}).get('y'))
    allocation_df['Latitude_Shel'] = allocation_df['Shelter Assigned'].map(lambda x: shel_dict.get(x, {}).get('x'))
    allocation_df['Longitude_Shel'] = allocation_df['Shelter Assigned'].map(lambda x: shel_dict.get(x, {}).get('y'))

    # Remove any rows with missing coordinates
    allocation_df.dropna(subset=['Latitude_Comm', 'Longitude_Comm', 'Latitude_Shel', 'Longitude_Shel'], inplace=True)

    avg_lat = (allocation_df['Latitude_Comm'].mean() + allocation_df['Latitude_Shel'].mean()) / 2
    avg_lon = (allocation_df['Longitude_Comm'].mean() + allocation_df['Longitude_Shel'].mean()) / 2
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=13)

    MousePosition(
        position="topright",
        separator=" | ",
        prefix="Coordinates:",
        lat_formatter="function(num) {return num.toFixed(6);}",
        lng_formatter="function(num) {return num.toFixed(6);}"
    ).add_to(m)

    # Add markers
    for _, row in allocation_df.iterrows():
        folium.Marker([row['Latitude_Comm'], row['Longitude_Comm']], popup=f"Community: {row['Community']}", icon=folium.Icon(color='green')).add_to(m)
        folium.Marker([row['Latitude_Shel'], row['Longitude_Shel']], popup=f"Shelter: {row['Shelter Assigned']}", icon=folium.Icon(color='blue')).add_to(m)

    # Define a bounding box for the region
    bbox_margin = 0.02
    bbox = (
        max(allocation_df['Latitude_Comm'].max(), allocation_df['Latitude_Shel'].max()) + bbox_margin,
        min(allocation_df['Latitude_Comm'].min(), allocation_df['Latitude_Shel'].min()) - bbox_margin,
        max(allocation_df['Longitude_Comm'].max(), allocation_df['Longitude_Shel'].max()) + bbox_margin,
        min(allocation_df['Longitude_Comm'].min(), allocation_df['Longitude_Shel'].min()) - bbox_margin
    )

    # Load the road graph for the region
    roadgraph = ox.graph_from_bbox(*bbox, network_type='all')

    # Precompute node coordinates for heuristic
    node_coords = {node: (data['y'], data['x']) for node, data in roadgraph.nodes(data=True)}

    def haversine_heuristic(u, v):
        lat1, lon1 = node_coords[u]
        lat2, lon2 = node_coords[v]
        return haversine_distance(lat1, lon1, lat2, lon2)
    
    used_shelters = list(set(allocation_df['Shelter Assigned']))
    route_layer = folium.FeatureGroup(name="Route Path")  # Follows the road network
    straight_layer = folium.FeatureGroup(name="Straight Path")  # Direct straight line

# Draw the route path (A* path)

    # Plot routes
    for idx, row in allocation_df.iterrows():
        try:
            start_node = ox.distance.nearest_nodes(roadgraph, row['Longitude_Comm'], row['Latitude_Comm'])
            end_node = ox.distance.nearest_nodes(roadgraph, row['Longitude_Shel'], row['Latitude_Shel'])
            start_location = (row['Latitude_Comm'], row['Longitude_Comm'])
            end_location = (row['Latitude_Shel'], row['Longitude_Shel'])
            shelter_id = used_shelters.index(row['Shelter Assigned'])
            

            route = nx.astar_path(roadgraph, start_node, end_node, heuristic=haversine_heuristic, weight='length')
            route_distance = sum(ox.utils_graph.get_route_edge_attributes(roadgraph, route, 'length'))
            route_coords = [(node_coords[node][0], node_coords[node][1]) for node in route]

            AntPath(route_coords, color=get_route_color(idx), weight=4, delay=800, popup=f"Route from {row['Community']} to {row['Shelter Assigned']} ({route_distance/1000:.2f} km)").add_to(route_layer)
            AntPath([start_location,end_location], color=get_route_color(shelter_id), weight=6, delay=800, popup=f"Route from {row['Community']} to {row['Shelter Assigned']} ({route_distance/1000:.2f} km)").add_to(straight_layer)

            print(f"Route from {row['Community']} to {row['Shelter Assigned']}: {route_distance / 1000:.2f} km")

        except nx.NetworkXNoPath:
            print(f"No path found from {row['Community']} to {row['Shelter Assigned']}.")
            continue
        except Exception as e:
            print(f"Error processing route from {row['Community']} to {row['Shelter Assigned']}: {e}")
            continue

    # Save map
    route_layer.add_to(m)
    straight_layer.add_to(m)
    folium.LayerControl(collapsed=False).add_to(m)
    m.save(os.path.join(save_dir,map_name))
    print(f"Map saved as {map_name}")
    return m

def load_data(file_path, expected_cols, alt_cols):
    df = pd.read_excel(file_path)
    for exp, alt in zip(expected_cols, alt_cols):
        if exp not in df.columns and alt in df.columns:
            df = df.rename(columns={alt: exp})
        return df

def run_optimization(communities_file='modelCommData.xlsx', shelters_file='modelShelData.xlsx', allocation_file='allocation_results.xlsx'):
    print("Running run_optimization")

    communities_path = os.path.join(save_dir, communities_file)
    shelters_path = os.path.join(save_dir, shelters_file)
    allocation_path = os.path.join(save_dir, allocation_file)

    # Load data
    communities_df = load_data(communities_path, 
                               expected_cols=["Name", "Longitude", "Latitude"], 
                               alt_cols=["Commmunity Longitude", "Commmunity Latitude"])
    communities_df = communities_df[["Name", "Longitude", "Latitude"]]
    
    shelters_df = load_data(shelters_path, 
                            expected_cols=["Name", "Longitude", "Latitude"], 
                            alt_cols=["Shelter Longitude", "Shelter Latitude"])
    shelters_df = shelters_df[["Name", "Longitude", "Latitude"]]

    allocation_df = pd.read_excel(os.path.join(save_dir, allocation_file), usecols=["Community", "Shelter Assigned"])

    # Create lookup dictionaries
    comm_dict = {row["Name"]: {"y": row["Longitude"], "x": row["Latitude"]} for _, row in communities_df.iterrows()}
    shel_dict = {row["Name"]: {"y": row["Longitude"], "x": row["Latitude"]} for _, row in shelters_df.iterrows()}

    # Plot the optimized routes
    plot_optimized_routes(allocation_df, comm_dict, shel_dict)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)  # Create application instance
    run_optimization()