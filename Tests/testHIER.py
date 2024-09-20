import random

#communities
Community = [
    {"name": "CommA", "population": 500, "distances_level1": {"Shel1A": 140, "Shel1B": 220}, "distances_level2": {"Shel2A": 1000, "Shel2B": 1800}},
    {"name": "CommB", "population": 400, "distances_level1": {"Shel1A": 530, "Shel1B": 2100}, "distances_level2": {"Shel2A": 500, "Shel2B": 1200}},
    {"name": "CommC", "population": 300, "distances_level1": {"Shel1A": 1210, "Shel1B": 420}, "distances_level2": {"Shel2A": 700, "Shel2B": 1100}},
    {"name": "CommD", "population": 200, "distances_level1": {"Shel1A": 620, "Shel1B": 320}, "distances_level2": {"Shel2A": 400, "Shel2B": 800}}
]

#shelters
Level1Shelter = [
    {"name": "Shel1A", "capacity": 800, "cost": 1000},
    {"name": "Shel1B", "capacity": 800, "cost": 1000}
]

Level2Shelter = [
    {"name": "Shel2A", "capacity": 1200, "cost": 2000},
    {"name": "Shel2B", "capacity": 1500, "cost": 2000}
]

weightDist = 0.5
weightCost = 0.5

#Assign to nearest level 1 shelter
def assign_communities_to_level1():
    ShelterCapacity = {shelter["name"]: shelter["capacity"] for shelter in Level1Shelter}
    assignments = {}

    for community in Community:
        available_shelters = list(community["distances_level1"].keys())
        available_shelters.sort(key=lambda x: community["distances_level1"][x])

        
        for shelter in available_shelters:
            if ShelterCapacity[shelter] >= community["population"]:
                assignments[community["name"]] = shelter
                ShelterCapacity[shelter] -= community["population"]
                break
        else:
            print(f"Warning: No available capacity for {community['name']} in level 1 shelters")

    return assignments

#Reassign to nearest level 2 shelter
def assign_communities_to_level2():
    ShelterCapacity = {shelter["name"]: shelter["capacity"] for shelter in Level2Shelter}
    assignments = {}

    for community in Community:
        available_shelters = list(community["distances_level2"].keys())
        available_shelters.sort(key=lambda x: community["distances_level2"][x])

        
        for shelter in available_shelters:
            if ShelterCapacity[shelter] >= community["population"]:
                assignments[community["name"]] = shelter
                ShelterCapacity[shelter] -= community["population"]
                break
        else:
            print(f"Warning: No available capacity for {community['name']} in level 2 shelters")

    return assignments


def calculate_fitness_level1(assignments):
    total_distance = 0
    total_cost = 0

    for community in Community:
        assigned_shelter = assignments.get(community["name"])
        if assigned_shelter:
            total_distance += community["distances_level1"][assigned_shelter]

    for shelter in Level1Shelter:
        total_cost += shelter["cost"]

    return weightDist * total_distance + weightCost * total_cost

def calculate_fitness_level2(assignments):
    total_distance = 0
    total_cost = 0

    for community in Community:
        assigned_shelter = assignments.get(community["name"])
        if assigned_shelter:
            total_distance += community["distances_level2"][assigned_shelter]

    for shelter in Level2Shelter:
        total_cost += shelter["cost"]

    return weightDist * total_distance + weightCost * total_cost

# Run HIER model
def hierarchical_location_allocation():
    level1_assignments = assign_communities_to_level1()
    fitness_level1 = calculate_fitness_level1(level1_assignments)
    
    print(f"Level 1 Assignments: {level1_assignments}")
    print(f"Level 1 Total fitness (cost + distance): {fitness_level1}")
    
    level2_assignments = assign_communities_to_level2()
    fitness_level2 = calculate_fitness_level2(level2_assignments)
    
    print(f"Level 2 Assignments: {level2_assignments}")
    print(f"Level 2 Total fitness (cost + distance): {fitness_level2}")

# Execute
hierarchical_location_allocation()
