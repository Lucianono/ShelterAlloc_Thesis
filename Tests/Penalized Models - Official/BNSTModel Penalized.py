# the official function for Bilevel Non-sequential Transfer model

from Calumpit_Data import Community,Shelters
import random
import copy
import numpy as np
import time

# TEMPORARY DUMMY DATA
# should be replaced with dynamic data from system
# simulation of area required per individual (meters squared), maximum no. of level 2 shelters
area_per_individual = 1
max_lvl2_shelters = 10
max_shelters = 10

solutions = []
num_generations = 200000
num_solutions = 100
mutation_rate = 0.2
mutation_iteration = 3

weight_dist = 0.5
weight_cost = 0.5
penalty_constant = 10**20

start_time = time.time()

# =======================
# SOLUTION SPAWNING
# create chromosome with randomized allocation
# chromosome are x2 in length, the second one are for transferred
def spawn():
    initial_allocations = {}
    transfer_allocations = {}
    shelter_lvl_assignment = {}

    for community in Community:
        shelter = random.choice(Shelters)["name"]
        initial_allocations[community["name"]] = shelter
        shelter = random.choice(Shelters)["name"]
        transfer_allocations[community["name"]] = shelter

    for shelter in Shelters:
        level = random.choice([1,2])
        shelter_lvl_assignment[shelter["name"]] = level

    allocations = {"initial": initial_allocations, "transferred": transfer_allocations, "shelterlvl": shelter_lvl_assignment}
    return allocations

# =======================
# OBJECTIVE FUNCTION
# also the fitness
# minimize fitness
def fitness(allocation):

    initial_shelters = set(allocation['initial'].values())
    transferred_shelters = set(allocation['transferred'].values())
    all_shelters = initial_shelters.union(transferred_shelters)

    Shelters_dict = {shelter["name"]: shelter for shelter in Shelters}

    total_distance = 0
    total_cost = 0

    for community in Community:
        # add distance * population
        shelter_name = allocation["initial"][community["name"]]
        distance = community["distances"][shelter_name]
        total_distance += distance * community["population"]

        #for transferring
        shelter_name_transfer = allocation["transferred"][community["name"]]
        shelter_dict = Shelters_dict.get(shelter_name)
        distance = shelter_dict["distances"][shelter_name_transfer]
        total_distance += distance * community["population"] * community["portiontransfer"]

    for shelter_name in all_shelters:
        # add cost based on shelter level
        shelter = Shelters_dict.get(shelter_name)
        if (allocation["shelterlvl"][shelter_name] == 1):
            total_cost += shelter["cost1"] 
        elif (allocation["shelterlvl"][shelter_name] == 2):
            total_cost += shelter["cost2"] 
        else:
            print("Shelter exceeded 2 levels. Something is wrong")
        
    # the actual model
    objective_value = weight_dist * total_distance + weight_cost * total_cost
    penalty_value = penalty_constant * getPenaltySum(allocation)

    return int(objective_value + penalty_value)

# =======================
# CONSTRAINTS
# maximum distance constraint (2.2)
def check_max_distance(allocation):

    penalty = 0

    for community in Community:
        shelter_name = allocation["initial"][community["name"]]
        distance = community["distances"][shelter_name]
        max_distance_community = community["maxdistance"]
        # check if distance is greater than max dist
        if (distance > max_distance_community):
            # print("maximum distance constraint failed")
            penalty += distance - max_distance_community
        
    return penalty

# initial capacity constraint (2.3)
def check_initial_capacity(allocation):
    shelter_areas = {shelter["name"]: shelter[f"area{allocation["shelterlvl"][shelter['name']]}"] for shelter in Shelters}
    used_area = {shelter["name"]: 0 for shelter in Shelters}

    penalty = 0

    for community in Community:
        shelter_name = allocation["initial"][community["name"]]
        if shelter_name:
            # add to used_area based on population
            required_area = community["population"] * area_per_individual
            used_area[shelter_name] += required_area

            #if used_area[shelter_name] > shelter_areas[shelter_name]:
                #print("initial capacity constraint failed")

    for shelter in Shelters:
        shelter_name = shelter["name"]
        penalty_value = used_area[shelter_name] - shelter_areas[shelter_name]
        penalty += max(0,penalty_value)

    return penalty

# capacity constraint for transfering (2.4)
def check_transferred_capacity(allocation):
    shelter_areas = {shelter["name"]: shelter["area2"] for shelter in Shelters}
    used_area = {shelter["name"]: 0 for shelter in Shelters}
    penalty = 0

    for community in Community:
        shelter_name = allocation["transferred"][community["name"]]
        if shelter_name:
            # add to used_area based on population
            required_area = community["population"] * community["portiontransfer"] * area_per_individual
            used_area[shelter_name] += required_area

            # if used_area[shelter_name] > shelter_areas[shelter_name]:
            #     # print("transferring capacity constraint failed")

    for shelter in Shelters:
        shelter_name = shelter["name"]
        penalty_value = used_area[shelter_name] - shelter_areas[shelter_name]
        penalty += max(0,penalty_value)

    return penalty


# max shelters to be constructed/allocated constraint (2.6)
def check_max_shelters(allocation):
    used_shelters = set() 
    penalty = 0

    for community in Community:
        shelter_name = allocation["initial"][community["name"]]
        used_shelters.add(shelter_name)  

    # If the number of unique shelters exceeds the max allowed
    if len(used_shelters) > max_shelters:
        # print("max shelters constraint failed")
        penalty += len(used_shelters) - max_shelters
            
    return penalty
        
# max lvl2 shelters to be constructed/allocated constraint (2.5)
def check_max_lvl2_shelters(allocation):
    
    lvl2_shelters_ctr = sum(1 for level in allocation["shelterlvl"].values() if level == 2)
    penalty = 0

    if lvl2_shelters_ctr > max_lvl2_shelters:
        # print("max lvl2 shelters constraint failed")
        penalty += lvl2_shelters_ctr - max_lvl2_shelters
   
    return penalty

# check if transferred shelter is lvl 2 (2.10)
def check_transfer_lvl2_shelters(allocation):
    transfered_shelters = set(allocation['transferred'].values())
    penalty = 0

    for shelter_name in transfered_shelters:
        if allocation["shelterlvl"][shelter_name] < 2:
            # print("transferred shelter is lvl 2 constraint failed")
            penalty += 1

    return penalty

# =======================
# CONSTRAINTS/PENALTY EXECUTION
# Check all constraints
def getPenaltySum(allocation):
     return (check_initial_capacity(allocation)**2 + 
            check_transferred_capacity(allocation)**2 + 
            check_max_distance(allocation)**2 + 
            check_max_shelters(allocation)**2 + 
            check_max_lvl2_shelters(allocation)**2 +
            check_transfer_lvl2_shelters(allocation)**2)

# =======================
# GENETIC ALGORITHM
# mutation operator
# TYPE : Random Reset
def mutate(allocation):
    new_allocations = copy.deepcopy(allocation)

    for _ in range(mutation_iteration) : 
        key_rand = random.choice(list(allocation.keys()))
        gene_to_mutate = random.choice(list(allocation[key_rand].keys()))
        current_value = allocation[key_rand][gene_to_mutate]
        
        if key_rand == "initial" or key_rand == "transferred":
            available_choices = [shelter["name"] for shelter in Shelters if shelter["name"] != current_value]
        elif key_rand == "shelterlvl":
            available_choices = [1,2]
            available_choices.remove(current_value)

        if available_choices:
            new_value = random.choice(available_choices)
            new_allocations[key_rand][gene_to_mutate] = new_value
            
    return new_allocations

# crossover operator
# TYPE : Uniform Crossover
def generate_offspring(parent1, parent2):
    offspring = {"initial":{},"transferred":{},"shelterlvl":{}}
    for community in Community:
        #for initial
        shelters = {parent1["initial"][community["name"]], parent2["initial"][community["name"]]} 
        
        if shelters:
            chosen_shelter = random.choice(list(shelters))
        else:
            chosen_shelter = random.choice([shelter["name"] for shelter in Shelters])

        offspring["initial"][community["name"]] = chosen_shelter

        #for transfer
        shelters = {parent1["transferred"][community["name"]], parent2["transferred"][community["name"]]} 
        
        if shelters:
            chosen_shelter = random.choice(list(shelters))
        else:
            chosen_shelter = random.choice([shelter["name"] for shelter in Shelters])

        offspring["transferred"][community["name"]] = chosen_shelter

    for shelter in Shelters:

        #for shelterlvl
        levels = {parent1["shelterlvl"][shelter["name"]], parent2["shelterlvl"][shelter["name"]]} 
        
        if shelters:
            chosen_lvl = random.choice(list(levels))
        else:
            chosen_lvl = random.choice([1,2])

        offspring["shelterlvl"][shelter["name"]] = chosen_lvl

    return offspring

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
    # Grouping communities by shelters for initial and transferred allocations
    grouped_by_shelter = {}

    for phase, allocations in allocation.items():
        if phase in ('initial', 'transferred'):
            for community, shelter in allocations.items():
                if shelter not in grouped_by_shelter:
                    grouped_by_shelter[shelter] = {'level': allocation['shelterlvl'].get(shelter, None), 'initial': [], 'transferred': []}
                grouped_by_shelter[shelter][phase].append(community)

    # Print the grouped data
    for shelter, details in grouped_by_shelter.items():
        print(f"Shelter: {shelter} (Level {details['level']})")
        print(f"  Initial:")
        for community in details['initial']:
            print(f"    - {community}")
        print(f"  Transferred:")
        for community in details['transferred']:
            print(f"    - {community}")
        print()


# =======================
# START OF THE ALGORITHM
# initial population
if not logicCheck():
    print("Parameters are inputted incorrectly.")
    exit()
if not feasibilityCheck():
    print("No solution exists")
    exit()

infeasibility_ctr = 0
generation_last_updated = 0

for _ in range(num_solutions):
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

    if (generation+1) % 100 == 0 :
        print(best_solutions[0])
        print(f"=== Gen {generation+1} best solution ===")

    prev_best_solution = fitness(solutions[0])

    # replace old population
    solutions = [sol[1] for sol in best_solutions]

    new_best_solution = fitness(solutions[0])

    #update generation_last_updated
    if(prev_best_solution != new_best_solution):
        generation_last_updated = generation+1


best_allocation = solutions[0]
show_allocation_details_grouped(best_allocation)
print(f"Generation when solution last updated : {generation_last_updated}")

# Calculate elapsed time
elapsed_time = time.time() - start_time

# Convert to minutes and seconds
minutes = int(elapsed_time // 60)
seconds = elapsed_time % 60

print(f"--- {minutes} minutes and {seconds:.2f} seconds ---")