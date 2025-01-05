# sample data of communities with barangay names along with population and distances from each shelter
Community = [
    {"name": "Comm1", "population": 10, "maxdistance": 5, 
     "distances": {
        "Shel1": 3.61, 
        "Shel2": 2.83, 
        "Shel3": 2.83,
        "Shel4": 3.61}, 
    "portiontransfer":0.5,
    "portionwork" : {
        "Work1" : 0.25
    }},
    {"name": "Comm2", "population": 10, "maxdistance": 5, 
     "distances": {
        "Shel1": 3.16, 
        "Shel2": 2.23, 
        "Shel3": 2.23,
        "Shel4": 3.16}, 
    "portiontransfer":0.5,
    "portionwork" : {
        "Work1" : 1
    }},
    {"name": "Comm3", "population": 10, "maxdistance": 5, 
     "distances": {
        "Shel1": 3, 
        "Shel2": 2, 
        "Shel3": 2,
        "Shel4": 3}, 
    "portiontransfer":0.5,
    "portionwork" : {
        "Work1" : 0.25
    }},
    {"name": "Comm4", "population": 10, "maxdistance": 5, 
     "distances": {
        "Shel1": 3.16, 
        "Shel2": 2.23, 
        "Shel3": 2.23,
        "Shel4": 3.16}, 
    "portiontransfer":0.5,
    "portionwork" : {
        "Work1" : 0.25
    }},
    {"name": "Comm5", "population": 10, "maxdistance": 5, 
     "distances": {
        "Shel1": 3.61, 
        "Shel2": 2.83, 
        "Shel3": 2.83,
        "Shel4": 3.61}, 
    "portiontransfer":0.5,
    "portionwork" : {
        "Work1" : 0.25
    }},
]

# list of shelters with area1 and cost1 (area and cost as level 1 shelter), area 2 and cost2 (area and cost as level 2 shelter) 
Shelters = [
    {"name": "Shel1", "area1": 40, "cost1": 40, "area2": 40, "cost2": 40, 
     "distances": {
        "Shel1": 0, 
        "Shel2": 1, 
        "Shel3": 5,
        "Shel4": 6
    },
    "distanceswork": {
         "Work1": 6.32
    }},
    {"name": "Shel2", "area1": 40, "cost1": 40, "area2": 40, "cost2": 40, 
     "distances": {
        "Shel1": 1, 
        "Shel2": 0, 
        "Shel3": 4,
        "Shel4": 5
    },
    "distanceswork": {
         "Work1": 5.39
    }},
    {"name": "Shel3", "area1": 40, "cost1": 40, "area2": 40, "cost2": 40, 
     "distances": {
        "Shel1": 5, 
        "Shel2": 4, 
        "Shel3": 0,
        "Shel4": 1
    },
    "distanceswork": {
         "Work1": 2.24
    }},
    {"name": "Shel4", "area1": 40, "cost1": 40, "area2": 40, "cost2": 40, 
     "distances": {
        "Shel1": 6, 
        "Shel2": 5, 
        "Shel3": 1,
        "Shel4": 0
    },
    "distanceswork": {
         "Work1": 2
    }},
]
