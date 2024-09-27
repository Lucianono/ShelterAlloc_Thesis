# the official function for Bilevel No Transfer model

import random
import numpy as np

# TEMPORARY DUMMY DATA
# should be replaced with dynamic data from system
area_per_individual = 1
max_lvl2_shelters = 2
max_shelters = 2

solutions = []
num_generations = 100
num_solutions = 1
mutation_rate = 0.5

weight_dist = 0.5
weight_cost = 0.5

Community = [
    {"name": "CommA", "population": 500, "maxdistance": 100, "distances": {"ShelA": 10, "ShelB": 20}},
    {"name": "CommB", "population": 400, "maxdistance": 100,  "distances": {"ShelA": 30, "ShelB": 20}},
    {"name": "CommC", "population": 300, "maxdistance": 100,  "distances": {"ShelA": 10, "ShelB": 20}}
]
Shelters = [
    {"name": "ShelA", "area1": 500, "cost1": 5000, "area2": 1000, "cost2": 6000},
    {"name": "ShelB", "area1": 300, "cost1": 4500, "area2": 800, "cost2": 5500},
]

# objective function, also the fitness
# minimize fitness
def fitness(allocation):

    shelter_areas_lvl1 = {shelter["name"]: shelter["area1"] for shelter in Shelters}
    shelter_areas_lvl2 = {shelter["name"]: shelter["area2"] for shelter in Shelters}
    used_area = {shelter["name"]: 0 for shelter in Shelters}

    total_distance = 0
    total_cost = 0

    for community in Community:
        # add distance
        shelter_name = allocation[community["name"]]
        distance = community["distances"][shelter_name]
        total_distance += distance

        # add to used_area based on population
        used_area[shelter_name] += community["population"] * area_per_individual

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

# capacity constraint
def check_capacity(allocation):
    shelter_areas_lvl2 = {shelter["name"]: shelter["area2"] for shelter in Shelters}
    used_area = {shelter["name"]: 0 for shelter in Shelters}

    for community in Community:
        shelter_name = allocation[community["name"]]
        if shelter_name:
            # add to used_area based on population
            required_area = community["population"] * area_per_individual
            used_area[shelter_name] += required_area

            if used_area[shelter_name] > shelter_areas_lvl2[shelter_name]:
                return False

    return True

# maximum distance constraint
def check_distance(allocation):

    for community in Community:
        shelter_name = allocation[community["name"]]
        distance = community["distances"][shelter_name]
        max_distance_community = community["maxdistance"]
        # check if distance is greater than max dist
        if (distance > max_distance_community):
            return False
        
    return True

# max shelters to be constructed/allocated constraint
def check_max_shelters(allocation):
    # Using a set since could detect uniqueness
    used_shelters = set() 
    for community in Community:
        shelter_name = allocation[community["name"]]
        used_shelters.add(shelter_name)  

        # If the number of unique shelters exceeds the max allowed
        if len(used_shelters) > max_shelters:
            return False
        
    return True

# count lvl 2 shelters opened 
def count_lvl2_shelters(allocation):
    shelter_areas_lvl1 = {shelter["name"]: shelter["area1"] for shelter in Shelters}
    used_area = {shelter["name"]: 0 for shelter in Shelters}
    
    # Calculate the used area for each shelter based on the allocation
    for community in Community:
        shelter_name = allocation[community["name"]]
        used_area[shelter_name] += community["population"] * area_per_individual
    
    # Count how many shelters have exceeded their level 1 area
    lvl2_shelters = 0
    for shelter in Shelters:
        shelter_name = shelter["name"]
        if used_area[shelter_name] > shelter_areas_lvl1[shelter_name]:
            lvl2_shelters += 1
    
    return lvl2_shelters


# max lvl2 shelters to be constructed/allocated constraint
def check_max_lvl2_shelters(allocation):
    return count_lvl2_shelters(allocation) <= max_lvl2_shelters

# Check all constraints
def checkConstraints(allocation):
     return (check_capacity(allocation) and 
            check_distance(allocation) and 
            check_max_shelters(allocation) and 
            check_max_lvl2_shelters(allocation))


# mutation operator
# TYPE : Swap Mutation
def mutate(allocation):
    community_to_mutate = random.choice(list(allocation.keys()))
    current_shelter = allocation[community_to_mutate]
    
    available_shelters = [shelter["name"] for shelter in Shelters if shelter["name"] != current_shelter]

    if available_shelters:
        new_shelter = random.choice(available_shelters)
        new_allocations = allocation.copy()
        new_allocations[community_to_mutate] = new_shelter
        
        return new_allocations if checkConstraints(new_allocations) else allocation

    return allocation

# crossover operator
# TYPE : Uniform Crossover
def generate_offspring(parent1, parent2):
    offspring = {}
    for community in Community:
        shelters = {parent1[community["name"]], parent2[community["name"]]} 
        
        if shelters:
            chosen_shelter = random.choice(list(shelters))
        else:
            chosen_shelter = random.choice([shelter["name"] for shelter in Shelters])

        while chosen_shelter not in [s["name"] for s in Shelters]:
            chosen_shelter = random.choice([shelter["name"] for shelter in Shelters])

        offspring[community["name"]] = chosen_shelter

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

# create individual with randomized allocation
def spawn():
    allocations = {}
    for community in Community:
        shelter = random.choice(Shelters)["name"]
        allocations[community["name"]] = shelter
    return allocations

# =======================
# START OF THE ALLGORITHM
# initial population
for _ in range(num_solutions):
    solution = spawn()
    while not checkConstraints(solution):
        solution = spawn()
    fitnessVal = fitness(solution)
    solutions.append(solution)

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
print("Opened Level 2 Shelters:" + str(count_lvl2_shelters(best_allocation)) )


