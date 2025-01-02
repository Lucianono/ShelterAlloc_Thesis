from PySide6.QtCore import QObject, Signal
import pandas as pd
import subprocess
import os

class PathfindingWorker(QObject):
    finished = Signal()
    progress = Signal(str)

    def __init__(self, community_file, shelter_file):
        super().__init__()
        self.community_file = community_file
        self.shelter_file = shelter_file
        self.cancelled = False

    def run(self):
        from plot_routes import plot_routes_on_map
        try:
            communities_df = pd.read_excel(self.community_file)
            shelters_df = pd.read_excel(self.shelter_file)

            self.progress.emit("Starting pathfinding...")
            
            plot_routes_on_map(communities_df, shelters_df, progress_callback=self.progress.emit)
            self.progress.emit("Pathfinding complete. Files saved.")

            self.progress.emit("Running genetic algorithm...")
            self.run_genetic_algorithm()
            self.progress.emit("Genetic algorithm completed.")

        except Exception as e:
            self.progress.emit(f"Error: {e}")
        finally:
            self.finished.emit()

    def cancel(self):
        self.cancelled = True

    def run_genetic_algorithm(self):

        community_file_path = os.path.join(os.getcwd(), "commData.xlsx")
        shelter_file_path = os.path.join(os.getcwd(), "shelData.xlsx")
        distance_file_path = os.path.join(os.getcwd(), "distance_matrix.xlsx")

        # Check if the files exist
        if not os.path.exists(community_file_path) or not os.path.exists(shelter_file_path) or not os.path.exists(distance_file_path):
            self.progress.emit("Error: Required input files are missing.")
            return
        
        # Run the genetic algorithm script
        try:
            # This runs the genetic algorithm in a separate process
            subprocess.run(["python", "BNTModel.py"], check=True)
        except subprocess.CalledProcessError as e:
            self.progress.emit(f"Error running genetic algorithm: {e}")
        except Exception as e:
            self.progress.emit(f"An unexpected error occurred: {e}")


