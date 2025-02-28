import pandas as pd
import os
import sys

class DataSets :
    # =======================
    # IMPORT DATA
    # get data and parameters from excel

    def get_community_data(self) :
        # sample data of communities with barangay names along with population and distances from each shelter
        self.save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")
        Community_data = pd.read_excel( os.path.join(self.save_dir, "modelCommData.xlsx") ).fillna("")
        Distances_data = pd.read_excel( os.path.join(self.save_dir, "distance_matrix.xlsx") ).fillna("")

        Community = []
        for row in Community_data.itertuples(index=False):
                # store all distances from community to all shleters
                distance_row_data = {}
                for _, shelter_row in Distances_data.iterrows():
                    shelter = shelter_row["Shelters"]  
                    distance = shelter_row[row.Name]  
                    distance_row_data[shelter] = distance  

                    
                # Extract community details and distance to shelters
                row_data = {
                    "name": row.Name,
                    "population": row.AffectedPop,
                    "maxdistance": row.MaxDistance,
                    "distances": distance_row_data
                }
                Community.append(row_data)

        return Community

    def get_shelter_data(self) :
         # list of shelters with area1 and cost1 (area and cost as level 1 shelter), area 2 and cost2 (area and cost as level 2 shelter) 
        self.save_dir = os.path.join(os.path.expanduser("~"), "Documents", "SLASystem")
        Shelter_data = pd.read_excel( os.path.join(self.save_dir, "modelShelData.xlsx") ).fillna("")
        
        Shelters = []
        for row in Shelter_data.itertuples(index=False):
                # Extract shelter details 
                row_data = {
                    "name": row.Name,
                    "area1": row.Area1,
                    "cost1": row.Cost1,
                    "area2": row.Area2,
                    "cost2": row.Cost2
                }
                Shelters.append(row_data)

        return Shelters








