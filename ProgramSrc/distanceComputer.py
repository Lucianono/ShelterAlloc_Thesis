
import pandas as pd
import osmnx as ox
import networkx as nx
from math import radians, cos, sin, sqrt, atan2
import sys, os


save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")

def plot_route(communities_df, shelters_df, excel_name="distance_matrix.xlsx"):
        bbox_margin = 0.01
        bbox = (
            max(communities_df['Latitude'].max(), shelters_df['Latitude'].max()) + bbox_margin,
            min(communities_df['Latitude'].min(), shelters_df['Latitude'].min()) - bbox_margin,
            max(communities_df['Longitude'].max(), shelters_df['Longitude'].max()) + bbox_margin,
            min(communities_df['Longitude'].min(), shelters_df['Longitude'].min()) - bbox_margin
        )

        roadgraph = ox.graph_from_bbox(*bbox, network_type='walk')
        node_coords = {node: (data['y'], data['x']) for node, data in roadgraph.nodes(data=True)}

        def haversine_heuristic(u, v):
            lat1, lon1 = node_coords[u]
            lat2, lon2 = node_coords[v]
            return haversine_distance(lat1, lon1, lat2, lon2)

        distance_matrix = pd.DataFrame(index=shelters_df['Name'], columns=communities_df['Name'], dtype=float)
        route_counter = 0

        for _, community in communities_df.iterrows():
            for _, shelter in shelters_df.iterrows():
                try:
                    start_node = ox.distance.nearest_nodes(roadgraph, community['Longitude'], community['Latitude'])
                    end_node = ox.distance.nearest_nodes(roadgraph, shelter['Longitude'], shelter['Latitude'])

                    route = nx.astar_path(roadgraph, start_node, end_node, heuristic=haversine_heuristic, weight='length')
                    route_distance = sum(ox.utils_graph.get_route_edge_attributes(roadgraph, route, 'length'))
                    distance_matrix.at[shelter['Name'], community['Name']] = route_distance / 1000  # Convert to km

                    route_counter += 1


                except nx.NetworkXNoPath:
                    continue
                except Exception as e:
                    continue

        distance_matrix.index.name = 'Shelters'
        distance_matrix.to_excel(os.path.join(save_dir,excel_name))

@staticmethod
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = radians(lat1), radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)
    a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
    return 2 * R * atan2(sqrt(a), sqrt(1 - a))



df1 = pd.read_excel(os.path.join(save_dir,"commData.xlsx"))
df2 = pd.read_excel(os.path.join(save_dir,"shelData.xlsx"))
plot_route(df1, df2)