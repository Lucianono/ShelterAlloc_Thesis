from PySide6.QtCore import QObject, Signal, QTimer
import pandas as pd
import subprocess
import os
import osmnx as ox
import folium
import networkx as nx
from math import radians, cos, sin, sqrt, atan2
from concurrent.futures import ThreadPoolExecutor, TimeoutError

class PathfindingWorker(QObject):
    finished = Signal()
    progress = Signal(str)
    feasibility_warning = Signal()

    def __init__(self, community_file, shelter_file):
        super().__init__()
        self.community_file = community_file
        self.shelter_file = shelter_file
        self.cancelled = False
        self.timer = QTimer(self)
        self.save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")

        self.timer.timeout.connect(self.check_for_cancel)

    def run(self):
        try:
            communities_df = pd.read_excel(os.path.join(self.save_dir,self.community_file))
            shelters_df = pd.read_excel(os.path.join(self.save_dir,self.shelter_file))

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
        
    


    def plot_route(self, communities_df, shelters_df, route_counter, map_name="all_routes_map.html", excel_name="distance_matrix.xlsx"):
        bbox_margin = 0.01
        bbox = (
            max(communities_df['Latitude'].max(), shelters_df['Latitude'].max()) + bbox_margin,
            min(communities_df['Latitude'].min(), shelters_df['Latitude'].min()) - bbox_margin,
            max(communities_df['Longitude'].max(), shelters_df['Longitude'].max()) + bbox_margin,
            min(communities_df['Longitude'].min(), shelters_df['Longitude'].min()) - bbox_margin
        )


        with ThreadPoolExecutor() as executor:
            future = executor.submit(ox.graph_from_bbox, *bbox, network_type='all')
            try:
                roadgraph = future.result(timeout=30)  # Wait for completion or timeout
            except TimeoutError:
                print("Fetching road graph took too long! Stopping...")
                self.cancelled = True
                roadgraph = None

        if roadgraph:
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
                    start_node = ox.distance.nearest_nodes(roadgraph, community['Longitude'], community['Latitude'])
                    end_node = ox.distance.nearest_nodes(roadgraph, shelter['Longitude'], shelter['Latitude'])

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
        distance_matrix.to_excel(os.path.join(self.save_dir,excel_name))
        self.progress.emit(f"Distance matrix saved as {excel_name}")



    @staticmethod
    def haversine_distance(lat1, lon1, lat2, lon2):
        R = 6371000
        phi1, phi2 = radians(lat1), radians(lat2)
        dphi = radians(lat2 - lat1)
        dlambda = radians(lon2 - lon1)
        a = sin(dphi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(dlambda / 2) ** 2
        return 2 * R * atan2(sqrt(a), sqrt(1 - a))
