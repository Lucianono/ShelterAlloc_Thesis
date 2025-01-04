# the official function for Bilevel Non-sequential Transfer model

import random
import copy
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

# =======================
# SOLUTION SPAWNING
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

# =======================
# OBJECTIVE FUNCTION
# also the fitness
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
            print("maximum distance constraint failed")
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
                print("initial capacity constraint failed")
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
                print("transfering capacity constraint failed")
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
            print("max shelters constraint failed")
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
    if count_lvl2_shelters(allocation) > max_lvl2_shelters:
        print("max lvl2 shelters constraint failed")
        return False
    else:
        return True

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
            print("transferred shelter is lvl 2 constraint failed")
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

# =======================
# GENETIC ALGORITHM
# mutation operator
# TYPE : Random Reset
def mutate(allocation):
    initial_or_transfer_rand = random.choice(list(allocation.keys()))
    community_to_mutate = random.choice(list(allocation[initial_or_transfer_rand].keys()))
    current_shelter = allocation[initial_or_transfer_rand][community_to_mutate]
    
    if initial_or_transfer_rand == "initial":
        available_shelters = [shelter["name"] for shelter in Shelters if shelter["name"] != current_shelter]
    elif initial_or_transfer_rand == "transferred":
        initial_shelters = set(allocation['initial'].values())
        available_shelters = [shelter for shelter in initial_shelters if shelter != current_shelter]

    if available_shelters:
        new_shelter = random.choice(available_shelters)
        new_allocations = copy.deepcopy(allocation)
        new_allocations[initial_or_transfer_rand][community_to_mutate] = new_shelter
        
        return new_allocations if checkConstraints(new_allocations) else allocation

    return allocation

# crossover operator
# TYPE : Uniform Crossover
def generate_offspring(parent1, parent2):
    offspring = {"initial":{},"transferred":{}}
    for community in Community:
        #for initial
        shelters = {parent1["initial"][community["name"]], parent2["initial"][community["name"]]} 
        
        if shelters:
            chosen_shelter = random.choice(list(shelters))
        else:
            chosen_shelter = random.choice([shelter["name"] for shelter in Shelters])

        while chosen_shelter not in [s["name"] for s in Shelters]:
            chosen_shelter = random.choice([shelter["name"] for shelter in Shelters])

        offspring["initial"][community["name"]] = chosen_shelter

        #for transfer
        shelters = {parent1["transferred"][community["name"]], parent2["transferred"][community["name"]]} 
        
        if shelters:
            chosen_shelter = random.choice(list(shelters))
        else:
            chosen_shelter = random.choice([shelter["name"] for shelter in Shelters])

        while chosen_shelter not in [s["name"] for s in Shelters]:
            chosen_shelter = random.choice([shelter["name"] for shelter in Shelters])

        offspring["transferred"][community["name"]] = chosen_shelter

    return offspring if checkConstraints(offspring) else parent1 

# selection operator
# TYPE : Roulette Wheel Selection
def selectParent(solutions):
    sum_fitness = sum(fitness for fitness, _ in solutions)
    inv_proportions = [sum_fitness/ fitness for fitness, _ in solutions]
    sum_inv_proportions = sum(inv_proportions)
    probability = [inv_proportion / sum_inv_proportions for inv_proportion in inv_proportions]
    solution_indices = np.arange(len(solutions))

    selected_solution = np.random.choice(solution_indices, p=probability)

    return solutions[selected_solution]

# =======================
# FEASIBILITY CHECK
# check if data input has solution
def feasibilityCheck():
    # check if there exists distance <= max distance 
    failing_communities = []
    for community in Community:
        if not any(d <= community["maxdistance"] for d in community["distances"].values()):
            failing_communities.append(community["name"])
    
    if failing_communities:
        print(f"{failing_communities} has maximum distance that is impossible to allocate. No shelters is close enough.")
        return False

    # check if there exists population <= shelter area * areaPerIndiv
    failing_communities = []
    for community in Community:
        if not (
            any(shelter["area1"] * area_per_individual >= community["population"] for shelter in Shelters) or
            any(shelter["area2"] * area_per_individual >= community["population"] for shelter in Shelters)
        ):
            failing_communities.append(community["name"])
    
    if failing_communities:
        print(f"{failing_communities} has affected population that is impossible to allocate. No shelters is large enough.")
        return False

    # check if total population is theoretically possible to allocate on largest  shelters
    total_population = sum(community['population'] for community in Community)

    Shelters_sorted = sorted(Shelters, key=lambda x: x['area2'], reverse=True)
    top_area2_sum = sum(shelter['area2'] for shelter in Shelters[:max_lvl2_shelters])
    Shelters_sorted = Shelters_sorted[max_lvl2_shelters:]

    Shelters_sorted = sorted(Shelters, key=lambda x: x['area1'], reverse=True)
    top_area1_sum = sum(shelter['area1'] for shelter in Shelters[:(max_shelters - max_lvl2_shelters)])
    Shelters_sorted = Shelters_sorted[(max_shelters - max_lvl2_shelters):]

    if total_population > (top_area2_sum + top_area1_sum):
        print(f"Total capacity of shelters available are less than the total affected population. Shelters has lower than expected capacity")
        return False
    
    # if no cases are violated return true
    return True

# =======================
# LOGIC CHECK
# check if parameters are logical or correct
def logicCheck():
    # check if max_shelters >= max_lvl2_shelters
    if max_shelters < max_lvl2_shelters:
        print("max_shelters should be greater than or equal to max_lvl2_shelters")
        return False
    # check if max_shelters >= 1
    if max_shelters < 1:
        print("max_shelters should have atleast 1")
        return False
    # check if area_per_individual > 0
    if area_per_individual <= 0:
        print("area_per_individual should be greater than 0")
        return False
    # check if num_generations >= 1
    if num_generations < 1:
        print("num_generations should be greater than or equal to 1")
        return False
    # check if num_solutions >= 1
    if num_solutions < 1:
        print("num_solutions should be greater than or equal to 1")
        return False
    # check if mutation_rate not < 0
    if mutation_rate < 0:
        print("mutation_rate should not be less than to 0")
        return False
    # check if weight_dist not < 0
    if weight_dist < 0:
        print("weight_dist should not be less than to 0")
        return False
    # check if weight_cost not < 0
    if weight_cost < 0:
        print("weight_cost should not be less than to 0")
        return False
    # check if area2 >= area1
    for shelter in Shelters:
        if shelter["area2"] < shelter["area1"]:
            print(f"{shelter['name']}: area2 should be grated than or equal to area1.")
            return False


    # if no cases are violated return true
        return True


# =======================
# DISPLAY ALLOCATION
def show_allocation_details_grouped(allocation):
    """
    Prints allocation details grouped by shelter for both 'initial' and 'transferred' stages.
    Includes communities allocated to each shelter, their populations, and shelter levels for 'initial' stage only.
    """
    # Precompute shelter areas
    shelter_areas = {
        shelter["name"]: {"lvl1": shelter["area1"], "lvl2": shelter["area2"]}
        for shelter in Shelters
    }

    # Function to group allocation details by shelter
    def group_allocation(stage_allocation, is_transferred=False):
        # Calculate used area for each shelter
        used_area = {shelter["name"]: 0 for shelter in Shelters}

        for community in Community:
            community_name = community["name"]
            population = community["population"]

            # Determine population for transferred stage
            if is_transferred:
                transferred_population = population * community["portiontransfer"]
                shelter_name = stage_allocation.get(community_name, None)
                if shelter_name:
                    used_area[shelter_name] += transferred_population
            else:
                shelter_name = stage_allocation[community_name]
                used_area[shelter_name] += population

        # Group by shelter
        shelters_details = {}
        for community in Community:
            community_name = community["name"]
            population = community["population"]

            if is_transferred:
                transferred_population = population * community["portiontransfer"]
                shelter_name = stage_allocation.get(community_name, None)
                actual_population = transferred_population
            else:
                shelter_name = stage_allocation[community_name]
                actual_population = population

            if not shelter_name:
                continue

            area_used = used_area[shelter_name]
            level = "Level 1" if area_used <= shelter_areas[shelter_name]["lvl1"] else "Level 2"

            if shelter_name not in shelters_details:
                shelters_details[shelter_name] = []

            details = {
                "community": community_name,
                "population": actual_population,
                "area_used": area_used,
            }
            if not is_transferred:
                details["level"] = level  # Add level only for the 'initial' stage

            shelters_details[shelter_name].append(details)

        return shelters_details

    # Iterate over allocation stages and print grouped details
    for stage_name, stage_allocation in allocation.items():
        is_transferred = stage_name == "transferred"
        print(f"\n=== Allocation Details for '{stage_name.capitalize()}' Stage ===")
        grouped_allocation = group_allocation(stage_allocation, is_transferred)

        for shelter_name, details in grouped_allocation.items():
            print(f"\nShelter: {shelter_name}")
            for detail in details:
                level_str = f", Shelter Level: {detail['level']}" if "level" in detail else ""
                print(f"  Community: {detail['community']}, "
                      f"Population: {detail['population']}, "
                      f"Used Area: {detail['area_used']}{level_str}")



test_alloc = {
    'initial':{
        'CommA' : 'ShelA',
        'CommB' : 'ShelB',
        'CommC' : 'ShelB',
    },
    'transferred':{
        'CommA' : 'ShelB',
        'CommB' : 'ShelB',
        'CommC' : 'ShelB',
    }
}
# print(show_allocation_details_grouped(test_alloc))

# =======================
# START OF THE ALGORITHM
# initial population
if not logicCheck():
    print("Parameters are not inputted incorrectly.")
    exit()
if not feasibilityCheck():
    print("No solution exists")
    exit()

infeasibility_ctr = 0
for _ in range(num_solutions):
    solution = spawn()
    while not checkConstraints(solution):
        infeasibility_ctr += 1
        # warning and halting
        if infeasibility_ctr >= 1000:
            print ("WARNING: 1000 infeasible solutions are generated. Program stopping.")
            exit()
        elif infeasibility_ctr % 500 == 0:
            print(f"WARNING: {infeasibility_ctr} infeasible solutions are generated. Program continuing.")

        solution = spawn()


    fitnessVal = fitness(solution)
    solutions.append(solution)
    infeasibility_ctr = 0

# generations
for generation in range(num_generations):

    # sorting from best to worst solutions
    ranked_solutions = [(fitness(sol), sol) for sol in solutions]
    ranked_solutions.sort(key=lambda x: x[0])

    # initiate selection and crossover
    new_population = []
    for i in range(num_solutions):
        mother = selectParent(ranked_solutions)[1]
        father = selectParent(ranked_solutions)[1]

        offspring = generate_offspring(mother, father)
        new_population.append(offspring)

    # initiate mutation
    mutated_population = []
    for solution in new_population:
        if random.random() < mutation_rate:
            solution = mutate(solution)
        mutated_population.append((fitness(solution),solution))

    # getting the top half solutions
    best_solutions = mutated_population + ranked_solutions
    best_solutions = sorted(best_solutions, key=lambda x: x[0])[:num_solutions] 

    print(f"=== Gen {generation} best solution ===")
    print(best_solutions[0])

    # replace old population
    solutions = [sol[1] for sol in best_solutions]


best_allocation = solutions[0]
show_allocation_details_grouped(best_allocation)
