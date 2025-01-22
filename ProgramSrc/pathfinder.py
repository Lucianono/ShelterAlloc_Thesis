from PySide6.QtCore import QObject, Signal, QTimer
import pandas as pd
import subprocess
import os
import osmnx as ox
import folium
import networkx as nx
from math import radians, cos, sin, sqrt, atan2

class PathfindingWorker(QObject):
    finished = Signal()
    progress = Signal(str)
    cancel_signal = Signal() 

    def __init__(self, community_file, shelter_file):
        super().__init__()
        self.community_file = community_file
        self.shelter_file = shelter_file
        self.cancelled = False
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.check_for_cancel)
        self.cancel_signal.connect(self.cancel)

    def run(self):
        try:
            communities_df = pd.read_excel(self.community_file)
            shelters_df = pd.read_excel(self.shelter_file)

            self.progress.emit("Starting pathfinding...")


            route_counter = 0
            for _, community in communities_df.iterrows():
                if self.cancelled:
                    self.progress.emit("Pathfinding cancelled during route calculation.")
                    return
                
                for _, shelter in shelters_df.iterrows():
                    if self.cancelled:
                        self.progress.emit("Pathfinding cancelled during route calculation.")
                        return
                    
                    try:
                        self.plot_route(communities_df, shelters_df, route_counter)
                        route_counter += 1
                        if not self.cancelled:
                            self.progress.emit("Pathfinding complete. Files saved.")
                            self.run_genetic_algorithm()
                        return
                    except Exception as e:
                        self.progress.emit(f"Error processing route from {community['Name']} to {shelter['Name']}: {e}")
                        continue

            

        except Exception as e:
            self.progress.emit(f"Error: {e}")
        finally:
            self.finished.emit()

    def cancel(self):
        self.cancelled = True

    def check_for_cancel(self):
        if self.cancelled:
            self.progress.emit("Cancelling operation...")
            self.timer.stop()
            self.finished.emit()
            return
        
    def run_genetic_algorithm(self):
        if self.cancelled:
            self.progress.emit("Genetic algorithm skipped due to cancellation.")
            return
        
        community_file_path = os.path.join(os.getcwd(), "commData.xlsx")
        shelter_file_path = os.path.join(os.getcwd(), "shelData.xlsx")
        distance_file_path = os.path.join(os.getcwd(), "distance_matrix.xlsx")

        if not os.path.exists(community_file_path) or not os.path.exists(shelter_file_path) or not os.path.exists(distance_file_path):
            self.progress.emit("Error: Required input files are missing.")
            return

        try:
            subprocess.run(["python", "BNTModelPenalized.py"], check=True)
        except subprocess.CalledProcessError as e:
            self.progress.emit(f"Error running genetic algorithm: {e}")
        except Exception as e:
            self.progress.emit(f"An unexpected error occurred: {e}")

    def plot_route(self, communities_df, shelters_df, route_counter, map_name="all_routes_map.html", excel_name="distance_matrix.xlsx"):
        bbox_margin = 0.01
        bbox = (
            max(communities_df['xDegrees'].max(), shelters_df['xDegrees'].max()) + bbox_margin,
            min(communities_df['xDegrees'].min(), shelters_df['xDegrees'].min()) - bbox_margin,
            max(communities_df['yDegrees'].max(), shelters_df['yDegrees'].max()) + bbox_margin,
            min(communities_df['yDegrees'].min(), shelters_df['yDegrees'].min()) - bbox_margin
        )

        roadgraph = ox.graph_from_bbox(*bbox, network_type='walk')
        node_coords = {node: (data['y'], data['x']) for node, data in roadgraph.nodes(data=True)}

        def haversine_heuristic(u, v):
            lat1, lon1 = node_coords[u]
            lat2, lon2 = node_coords[v]
            return self.haversine_distance(lat1, lon1, lat2, lon2)

        distance_matrix = pd.DataFrame(index=shelters_df['Name'], columns=communities_df['Name'], dtype=float)
        route_counter = 0

        for _, community in communities_df.iterrows():
            if self.cancelled:
                self.progress.emit("Pathfinding cancelled.")
                return
            for _, shelter in shelters_df.iterrows():
                if self.cancelled:
                    self.progress.emit("Pathfinding cancelled.")
                    return
                try:
                    start_node = ox.distance.nearest_nodes(roadgraph, community['yDegrees'], community['xDegrees'])
                    end_node = ox.distance.nearest_nodes(roadgraph, shelter['yDegrees'], shelter['xDegrees'])

                    route = nx.astar_path(roadgraph, start_node, end_node, heuristic=haversine_heuristic, weight='length')
                    route_distance = sum(ox.utils_graph.get_route_edge_attributes(roadgraph, route, 'length'))
                    distance_matrix.at[shelter['Name'], community['Name']] = route_distance / 1000  # Convert to km

                    route_counter += 1

                    self.progress.emit(f"Route from {community['Name']} to {shelter['Name']} completed: {route_distance / 1000:.2f} km")

                except nx.NetworkXNoPath:
                    self.progress.emit(f"No path found from {community['Name']} to {shelter['Name']}.")
                    continue
                except Exception as e:
                    self.progress.emit(f"Error processing route from {community['Name']} to {shelter['Name']}: {e}")
                    continue

        distance_matrix.index.name = 'Shelters'
        distance_matrix.to_excel(excel_name)
        self.progress.emit(f"Distance matrix saved as {excel_name}")

    @staticmethod
    def haversine_distance(lat1, lon1, lat2, lon2):
        R = 6371000
        phi1, phi2 = radians(lat1), radians(lat2)
        dphi = radians(lat2 - lat1)
        dlambda = radians(lon2 - lon1)
        a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
        return 2 * R * atan2(sqrt(a), sqrt(1 - a))
