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
save_dir = os.path.join(os.getcwd())

def get_route_color(iteration_index):
    return ROUTE_COLORS[iteration_index % len(ROUTE_COLORS)]

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
    
    used_shelters = list(set(allocation_df['Shelter Assigned']))
    straight_layer = folium.FeatureGroup(name="Straight Path")  # Direct straight line

# Draw the route path (A* path)

    # Plot routes
    for idx, row in allocation_df.iterrows():
        try:
            start_location = (row['Latitude_Comm'], row['Longitude_Comm'])
            end_location = (row['Latitude_Shel'], row['Longitude_Shel'])
            shelter_id = used_shelters.index(row['Shelter Assigned'])

            AntPath([start_location,end_location], color=get_route_color(shelter_id), weight=6, delay=800).add_to(straight_layer)

        except nx.NetworkXNoPath:
            print(f"No path found from {row['Community']} to {row['Shelter Assigned']}.")
            continue
        except Exception as e:
            print(f"Error processing route from {row['Community']} to {row['Shelter Assigned']}: {e}")
            continue

    # Save map
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

    allocation_df = pd.read_excel(allocation_path, usecols=["Community", "Shelter Assigned"])

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