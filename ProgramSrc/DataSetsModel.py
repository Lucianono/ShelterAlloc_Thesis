import pandas as pd
import os

# =======================
# IMPORT DATA
# get data and parameters from excel
Community_data = pd.read_excel( os.path.join(os.getcwd(), "commData.xlsx") ).fillna("")
Shelter_data = pd.read_excel( os.path.join(os.getcwd(), "shelData.xlsx") ).fillna("")
Distances_data = pd.read_excel( os.path.join(os.getcwd(), "distance_matrix.xlsx") ).fillna("")

if 'Active' not in Community_data.columns:
    Community_data['Active'] = False
Community_data_active = Community_data[Community_data['Active'] == True]

if 'Active' not in Shelter_data.columns:
    Shelter_data['Active'] = False
Shelter_data_active = Shelter_data[Shelter_data['Active'] == True]

# Combined filtering function
def filter_shelters(
    Shelter_data_active,
    flood_switch_state=False,
    typhoon_switch_state=False,
    earthquake_switch_state=False,
    built_switch_state=False,
    partially_built_switch_state=False,
    damaged_switch_state=False,
    empty_lot_switch_state=False
):
    # Ensure consistent boolean types for resistance filtering
    Shelter_data_active.loc[:, "ResToFlood"] = Shelter_data_active["ResToFlood"].map(lambda x: str(x).strip().upper() == "TRUE")
    Shelter_data_active.loc[:, "ResToTyphoon"] = Shelter_data_active["ResToTyphoon"].map(lambda x: str(x).strip().upper() == "TRUE")
    Shelter_data_active.loc[:, "ResToEarthquake"] = Shelter_data_active["ResToEarthquake"].map(lambda x: str(x).strip().upper() == "TRUE")
    
    # Filter by resistance
    if flood_switch_state:
        Shelter_data_active = Shelter_data_active[Shelter_data_active["ResToFlood"]]
    if typhoon_switch_state:
        Shelter_data_active = Shelter_data_active[Shelter_data_active["ResToTyphoon"]]
    if earthquake_switch_state:
        Shelter_data_active = Shelter_data_active[Shelter_data_active["ResToEarthquake"]]
    
    # Filter by shelter status
    status_conditions = []
    if built_switch_state:
        status_conditions.append("Built")
    if partially_built_switch_state:
        status_conditions.append("Partially Built")
    if damaged_switch_state:
        status_conditions.append("Damaged")
    if empty_lot_switch_state:
        status_conditions.append("Empty Lot")
    
    if status_conditions:
        # Ensure case-insensitive and whitespace-trimmed comparison for the "Status" column
        Shelter_data_active["Status"] = Shelter_data_active["Status"].fillna("").astype(str)
        Shelter_data_active = Shelter_data_active[
            Shelter_data_active["Status"].str.strip().str.title().isin(status_conditions)
        ]

    return Shelter_data_active

# Test the filtering
filtered_shelters = filter_shelters(
    Shelter_data_active,
    flood_switch_state=True,
    typhoon_switch_state=True,
    earthquake_switch_state=True,
    built_switch_state=False,
    partially_built_switch_state=True,
    damaged_switch_state=False,
    empty_lot_switch_state=False
)

# list of shelters with area1 and cost1 (area and cost as level 1 shelter), area 2 and cost2 (area and cost as level 2 shelter) 
Shelters = []
for row in filtered_shelters.itertuples(index=False):
        # Extract shelter details 
        row_data = {
            "name": row.Name,
            "area1": row.Area1,
            "cost1": row.Cost1,
            "area2": row.Area2,
            "cost2": row.Cost2
        }
        Shelters.append(row_data)

# sample data of communities with barangay names along with population and distances from each shelter
Community = []
for row in Community_data_active.itertuples(index=False):
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

