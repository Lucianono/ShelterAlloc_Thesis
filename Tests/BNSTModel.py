# the official function for Bilevel Non-sequential Transfer model

import random
import numpy as np

# TEMPORARY DUMMY DATA
# should be replaced with dynamic data from system
# simulation of area required per individual (meters squared), maximum no. of level 2 shelters
area_per_individual = 1
max_lvl2_shelters = 10
max_shelters = 10

solutions = []
num_generations = 100
num_solutions = 20
mutation_rate = 0.5

weight_dist = 0.5
weight_cost = 0.5

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


# create chromosome with randomized allocation
# chromosome are x2 in length, the second one are for transferred
def spawn():
    initial_allocations = {}
    transfer_allocations = {}
    opened_shelters = set() 

    for community in Community:
        shelter = random.choice(Shelters)["name"]
        initial_allocations[community["name"]] = shelter
        opened_shelters.add(shelter)  
    for community in Community:
        shelter = random.choice(list(opened_shelters))
        transfer_allocations[community["name"]] = shelter

    allocations = {"initial": initial_allocations, "transferred": transfer_allocations}
    return allocations


# objective function, also the fitness
# minimize fitness
def fitness(allocation):

    shelter_areas_lvl1 = {shelter["name"]: shelter["area1"] for shelter in Shelters}
    shelter_areas_lvl2 = {shelter["name"]: shelter["area2"] for shelter in Shelters}
    used_area = {shelter["name"]: 0 for shelter in Shelters}
    Shelters_dict = {shelter["name"]: shelter for shelter in Shelters}

    total_distance = 0
    total_cost = 0

    for community in Community:
        # add distance * population
        shelter_name = allocation["initial"][community["name"]]
        shelter_dict = Shelters_dict.get(shelter_name)
        distance = community["distances"][shelter_name]
        total_distance += distance * community["population"]

        # add to used_area based on population
        used_area[shelter_name] += community["population"] * area_per_individual

        #for transferring
        shelter_name_transfer = allocation["transferred"][community["name"]]
        distance = shelter_dict["distances"][shelter_name_transfer]
        total_distance += distance * community["population"] * community["portiontransfer"]

    for shelter in Shelters:
        # add cost based on used area
        shelter_name = shelter["name"]
        used_area_val = used_area[shelter_name]
        if(used_area_val == 0):
            continue
        elif(used_area_val <= shelter_areas_lvl1[shelter_name]):
            total_cost += shelter["cost1"]
        elif (used_area_val <= shelter_areas_lvl2[shelter_name]):
            total_cost += shelter["cost2"]
        else:
            print("Area usage exceeded to capacity of shelter. Constraints are wrong")
        
    # the actual model
    return weight_dist * total_distance + weight_cost * total_cost

# =======================
# CONSTRAINTS
# maximum distance constraint (2.2)
def check_max_distance(allocation):

    for community in Community:
        shelter_name = allocation["initial"][community["name"]]
        distance = community["distances"][shelter_name]
        max_distance_community = community["maxdistance"]
        # check if distance is greater than max dist
        if (distance > max_distance_community):
            return False
        
    return True

# initial capacity constraint (2.3)
def check_initial_capacity(allocation):
    shelter_areas_lvl2 = {shelter["name"]: shelter["area2"] for shelter in Shelters}
    used_area = {shelter["name"]: 0 for shelter in Shelters}

    for community in Community:
        shelter_name = allocation["initial"][community["name"]]
        if shelter_name:
            # add to used_area based on population
            required_area = community["population"] * area_per_individual
            used_area[shelter_name] += required_area

            if used_area[shelter_name] > shelter_areas_lvl2[shelter_name]:
                return False

    return True

# capacity constraint for transfering (2.4)
def check_transferred_capacity(allocation):
    shelter_areas_lvl2 = {shelter["name"]: shelter["area2"] for shelter in Shelters}
    used_area = {shelter["name"]: 0 for shelter in Shelters}

    for community in Community:
        shelter_name = allocation["transferred"][community["name"]]
        if shelter_name:
            # add to used_area based on population
            required_area = community["population"] * community["portiontransfer"] * area_per_individual
            used_area[shelter_name] += required_area

            if used_area[shelter_name] > shelter_areas_lvl2[shelter_name]:
                return False

    return True

# max shelters to be constructed/allocated constraint (2.6)
def check_max_shelters(allocation):
    # Using a set since could detect uniqueness
    used_shelters = set() 
    for community in Community:
        shelter_name = allocation["initial"][community["name"]]
        used_shelters.add(shelter_name)  

        # If the number of unique shelters exceeds the max allowed
        if len(used_shelters) > max_shelters:
            return False
        
    return True

# count lvl 2 shelters opened (2.5)
def count_lvl2_shelters(allocation):
    shelter_areas_lvl1 = {shelter["name"]: shelter["area1"] for shelter in Shelters}
    used_area = {shelter["name"]: 0 for shelter in Shelters}
    
    # Calculate the used area for each shelter based on the allocation
    for community in Community:
        shelter_name = allocation["initial"][community["name"]]
        used_area[shelter_name] += community["population"] * area_per_individual
    
    # Count how many shelters have exceeded their level 1 area
    lvl2_shelters = 0
    for shelter in Shelters:
        shelter_name = shelter["name"]
        if used_area[shelter_name] > shelter_areas_lvl1[shelter_name]:
            lvl2_shelters += 1
    
    return lvl2_shelters
# max lvl2 shelters to be constructed/allocated constraint (2.26)
def check_max_lvl2_shelters(allocation):
    return count_lvl2_shelters(allocation) <= max_lvl2_shelters

# check if transferred shelter is lvl 2 (2.10)
def check_transfer_lvl2_shelters(allocation):
    shelter_areas_lvl1 = {shelter["name"]: shelter["area1"] for shelter in Shelters}
    used_area = {shelter["name"]: 0 for shelter in Shelters}
    transfered_shelters = set()
    
    # Calculate the used area for each shelter based on the allocation
    for community in Community:
        shelter_name = allocation["initial"][community["name"]]
        used_area[shelter_name] += community["population"] * area_per_individual
        transfered_shelters.add(allocation["transferred"][community["name"]])
    
    # Return false if a transfer shelter is lvl 1
    for shelter in Shelters:
        shelter_name = shelter["name"]
        if (used_area[shelter_name] <= shelter_areas_lvl1[shelter_name] and 
            shelter_name in transfered_shelters):
            return False

    return True

# =======================
# CONSTRAINTS EXECUTION
# Check all constraints
def checkConstraints(allocation):
     return (check_initial_capacity(allocation) and 
            check_transferred_capacity(allocation) and 
            check_max_distance(allocation) and 
            check_max_shelters(allocation) and 
            check_max_lvl2_shelters(allocation) and
            check_transfer_lvl2_shelters(allocation))

test_alloc = {
    'initial':{
        'CommA' : 'ShelA',
        'CommB' : 'ShelB',
        'CommC' : 'ShelB',
    },
    'transferred':{
        'CommA' : 'ShelA',
        'CommB' : 'ShelB',
        'CommC' : 'ShelB',
    }
}
print(checkConstraints(test_alloc))