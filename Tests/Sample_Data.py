# sample data of communities with barangay names along with population and distances from each shelter
Community = [
    {"name": "CommA", "population": 500, "maxdistance": 100, "distances": {
        "ShelA": 10, 
        "ShelB": 20}, 
        "portiontransfer":.5,},
    
    {"name": "CommB", "population": 400, "maxdistance": 100, "distances": {
        "ShelA": 30, 
        "ShelB": 20}, 
        "portiontransfer":0.5,},

    {"name": "CommC", "population": 300, "maxdistance": 100, "distances": {
        "ShelA": 10, 
        "ShelB": 20}, 
        "portiontransfer":0.5,},
]

# list of shelters with area1 and cost1 (area and cost as level 1 shelter), area 2 and cost2 (area and cost as level 2 shelter) 
Shelters = [
    {"name": "ShelA", "area1": 500, "cost1": 5000, "area2": 1000, "cost2": 6000, 
     "distances": {
         "ShelA": 0, 
         "ShelB": 10
     }},

     {"name": "ShelB", "area1": 300, "cost1": 4500, "area2": 800, "cost2": 5500, 
     "distances": {
         "ShelA": 10, 
         "ShelB": 0
     }},
    
]