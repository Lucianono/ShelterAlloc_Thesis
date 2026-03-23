


import pandas as pd

# Your big dictionary here
data = {'initial': {'Aya': 'City EC of Sto. Tomas', 'Banga & San Guillermo': 'Suplang Covered Court', 'Caloocan & Leynes': 'San Antonio Brgy. Hall', 'Poblacion Barangay 1': 'Brgy. Asis-3 EC', 'Poblacion Barangay 5': 'Santa Clara Brgy. Hall', 'Poblacion Barangay 2,3,4,6,7,8': 'Brgy. San Jose BB Court', 'Quiling, Miranda, & Tumaway': 'Maugat Gymnasium', 'Sampaloc': 'San Fernando Brgy. Hall', 'Santa Maria, Balas, & Buco': 'Tagaytay Unida Church', 'Tranca': 'Darasa Brgy. Hall'}, 'transferred': {'Aya': 'City EC of Sto. Tomas', 'Banga & San Guillermo': 'City EC of Sto. Tomas', 'Caloocan & Leynes': 'Maugat Gymnasium', 'Poblacion Barangay 1': 'Maugat Gymnasium', 'Poblacion Barangay 5': 'City EC of Sto. Tomas', 'Poblacion Barangay 2,3,4,6,7,8': 'City EC of Sto. Tomas', 'Quiling, Miranda, & Tumaway': 'Maugat Gymnasium', 'Sampaloc': 'Maugat Gymnasium', 'Santa Maria, Balas, & Buco': 'Maugat Gymnasium', 'Tranca': 'Maugat Gymnasium'}, 'shelterlvl': {'San Fernando Brgy. Hall': 1, 'Santa Clara Brgy. Hall': 1, 'Darasa Brgy. Hall': 1, 'San Antonio Brgy. Hall': 1, 'Tagaytay Unida Church': 1, 'Maugat Gymnasium': 1, 'Brgy. San Jose BB Court': 1, 'Suplang Covered Court': 1, 'City EC of Sto. Tomas': 2, 'Brgy. Asis-3 EC': 1}}



df = pd.DataFrame([
    {
        "Community": community,
        "Shelter Initial": initial_shelter,
        "Shelter Level": data['shelterlvl'].get(initial_shelter),
        "Shelter Transfer": data['transferred'].get(community),
        "Shelter Level (Transfer)": data['shelterlvl'].get(data['transferred'].get(community))
    
    }
    for community, initial_shelter in data['initial'].items()

])

# Save to Excel
df.to_excel("Talisay Simulation/BST_alloc.xlsx", index=False)
print("Excel file created: ALLOC.xlsx")
