# the official function for Bilevel No Transfer model

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
    {"name": "Aya", "population": 6215, "maxdistance": 570, "distances": {
        "Brgy. Asis-3 EC": 374.90, "City EC of Sto. Tomas": 197.28, "Suplang Covered Court": 151.16,
        "Brgy. San Jose BB Court": 62.86, "Maugat Gymnasium": 64.26, "Tagaytay Unida Church": 272.00,
        "San Antonio Brgy. Hall": 233.10, "Darasa Brgy. Hall": 242.71, "Santa Clara Brgy. Hall": 367.89, 
        "San Fernando Brgy. Hall": 302.74}},
    
    {"name": "Banga & San Guillermo", "population": 5116, "maxdistance": 570, "distances": {
        "Brgy. Asis-3 EC": 268.72, "City EC of Sto. Tomas": 303.71, "Suplang Covered Court": 200.81,
        "Brgy. San Jose BB Court": 159.09, "Maugat Gymnasium": 170.07, "Tagaytay Unida Church": 166.00,
        "San Antonio Brgy. Hall": 339.18, "Darasa Brgy. Hall": 345.62, "Santa Clara Brgy. Hall": 468.00, 
        "San Fernando Brgy. Hall": 402.38}},
    
    {"name": "Calocan & Leynes", "population": 3258, "maxdistance": 570, "distances": {
        "Brgy. Asis-3 EC": 208.44, "City EC of Sto. Tomas": 369.01, "Suplang Covered Court": 264.84,
        "Brgy. San Jose BB Court": 228.38, "Maugat Gymnasium": 237.39, "Tagaytay Unida Church": 109.49,
        "San Antonio Brgy. Hall": 406.17, "Darasa Brgy. Hall": 405.44, "Santa Clara Brgy. Hall": 524.12, 
        "San Fernando Brgy. Hall": 458.62}},
    
    {"name": "Poblacion Barangay 1", "population": 1921, "maxdistance": 570, "distances": {
        "Brgy. Asis-3 EC": 312.82, "City EC of Sto. Tomas": 261.91, "Suplang Covered Court": 192.62,
        "Brgy. San Jose BB Court": 127.45, "Maugat Gymnasium": 131.45, "Tagaytay Unida Church": 210.74,
        "San Antonio Brgy. Hall": 299.48, "Darasa Brgy. Hall": 300.36, "Santa Clara Brgy. Hall": 421.82, 
        "San Fernando Brgy. Hall": 356.18}},
    
    {"name": "Poblacion Barangay 5", "population": 265, "maxdistance": 570, "distances": {
        "Brgy. Asis-3 EC": 294.99, "City EC of Sto. Tomas": 279.31, "Suplang Covered Court": 209.12,
        "Brgy. San Jose BB Court": 142.84, "Maugat Gymnasium": 147.11, "Tagaytay Unida Church": 194.65,
        "San Antonio Brgy. Hall": 315.62, "Darasa Brgy. Hall": 310.37, "Santa Clara Brgy. Hall": 432.52, 
        "San Fernando Brgy. Hall": 366.90}},
    
    {"name": "Poblacion Barangay 2,3,4,6,7,8", "population": 8073, "maxdistance": 570, "distances": {
        "Brgy. Asis-3 EC": 298.87, "City EC of Sto. Tomas": 281.48, "Suplang Covered Court": 205.87,
        "Brgy. San Jose BB Court": 137.50, "Maugat Gymnasium": 141.88, "Tagaytay Unida Church": 192.46,
        "San Antonio Brgy. Hall": 311.57, "Darasa Brgy. Hall": 308.53, "Santa Clara Brgy. Hall": 429.73, 
        "San Fernando Brgy. Hall": 364.07}},
    
    {"name": "Quiling, Miranda, & Tumaway", "population": 9050, "maxdistance": 570, "distances": {
        "Brgy. Asis-3 EC": 329.97, "City EC of Sto. Tomas": 242.34, "Suplang Covered Court": 166.72,
        "Brgy. San Jose BB Court": 101.59, "Maugat Gymnasium": 109.04, "Tagaytay Unida Church": 227.14,
        "San Antonio Brgy. Hall": 278.09, "Darasa Brgy. Hall": 285.72, "Santa Clara Brgy. Hall": 409.55, 
        "San Fernando Brgy. Hall": 344.08}},
    
    {"name": "Sampaloc", "population": 4531, "maxdistance": 570, "distances": {
        "Brgy. Asis-3 EC": 167.19, "City EC of Sto. Tomas": 420.32, "Suplang Covered Court": 316.14,
        "Brgy. San Jose BB Court": 282.04, "Maugat Gymnasium": 290.10, "Tagaytay Unida Church": 81.61,
        "San Antonio Brgy. Hall": 458.41, "Darasa Brgy. Hall": 453.42, "Santa Clara Brgy. Hall": 569.31, 
        "San Fernando Brgy. Hall": 504.14}},
    
    {"name": "Santa Maria, Balas, & Buco", "population": 3922, "maxdistance": 570, "distances": {
        "Brgy. Asis-3 EC": 263.79, "City EC of Sto. Tomas": 314.29, "Suplang Covered Court": 231.04,
        "Brgy. San Jose BB Court": 178.84, "Maugat Gymnasium": 184.40, "Tagaytay Unida Church": 163.44,
        "San Antonio Brgy. Hall": 352.34, "Darasa Brgy. Hall": 349.80, "Santa Clara Brgy. Hall": 468.83, 
        "San Fernando Brgy. Hall": 403.27}},
    
    {"name": "Tranca", "population": 2950, "maxdistance": 570, "distances": {
        "Brgy. Asis-3 EC": 377.92, "City EC of Sto. Tomas": 214.54, "Suplang Covered Court": 76.48,
        "Brgy. San Jose BB Court": 59.50, "Maugat Gymnasium": 91.75, "Tagaytay Unida Church": 277.14,
        "San Antonio Brgy. Hall": 238.34, "Darasa Brgy. Hall": 276.74, "Santa Clara Brgy. Hall": 404.33, 
        "San Fernando Brgy. Hall": 341.93}}
]

# list of shelters with area1 and cost1 (area and cost as level 1 shelter), area 2 and cost2 (area and cost as level 2 shelter) 
Shelters = [
    {"name": "Brgy. Asis-3 EC", "area1": 10000, "cost1": 10000, "area2": 20000, "cost2": 20000},
    {"name": "City EC of Sto. Tomas", "area1": 10000, "cost1": 10000, "area2": 20000, "cost2": 20000},
    {"name": "Suplang Covered Court", "area1": 10000, "cost1": 10000, "area2": 20000, "cost2": 20000},
    {"name": "Brgy. San Jose BB Court", "area1": 10000, "cost1": 10000, "area2": 20000, "cost2": 20000},
    {"name": "Maugat Gymnasium", "area1": 10000, "cost1": 10000, "area2": 20000, "cost2": 20000},
    {"name": "Tagaytay Unida Church", "area1": 10000, "cost1": 10000, "area2": 20000, "cost2": 20000},
    {"name": "San Antonio Brgy. Hall", "area1": 10000, "cost1": 10000, "area2": 20000, "cost2": 20000},
    {"name": "Darasa Brgy. Hall", "area1": 10000, "cost1": 10000, "area2": 20000, "cost2": 20000},
    {"name": "Santa Clara Brgy. Hall", "area1": 10000, "cost1": 10000, "area2": 20000, "cost2": 20000},
    {"name": "San Fernando Brgy. Hall", "area1": 10000, "cost1": 10000, "area2": 20000, "cost2": 20000},
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
        # add distance * population
        shelter_name = allocation[community["name"]]
        distance = community["distances"][shelter_name]
        total_distance += distance * community["population"]

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

# print allocations
def show_allocation_details_grouped(allocation):
    """
    Prints the details of an allocation grouped by shelter,
    including the communities allocated to each shelter,
    their populations, and whether it's a Level 1 or Level 2 shelter.
    """
    shelter_areas_lvl1 = {shelter["name"]: shelter["area1"] for shelter in Shelters}
    shelter_areas_lvl2 = {shelter["name"]: shelter["area2"] for shelter in Shelters}
    
    # Calculate the used area for each shelter based on the allocation
    used_area = {shelter["name"]: 0 for shelter in Shelters}
    for community in Community:
        shelter_name = allocation[community["name"]]
        used_area[shelter_name] += community["population"] * area_per_individual

    # Grouping by shelter
    shelters_details = {}
    
    for community in Community:
        shelter_name = allocation[community["name"]]
        population = community["population"]
        area_used = used_area[shelter_name]
        
        # Determine shelter level
        level = "Level 1" if area_used <= shelter_areas_lvl1[shelter_name] else "Level 2"
        
        if shelter_name not in shelters_details:
            shelters_details[shelter_name] = []
        
        shelters_details[shelter_name].append({
            "community": community["name"],
            "population": population,
            "area_used": area_used,
            "level": level
        })

    print("=== Allocation Details Grouped by Shelter ===")
    for shelter_name, details in shelters_details.items():
        print(f"\nShelter: {shelter_name}")
        for detail in details:
            print(f"  Community: {detail['community']}, "
                  f"Population: {detail['population']}, "
                  f"Used Area: {detail['area_used']}, "
                  f"Shelter Level: {detail['level']}")

# capacity constraint (2.25)
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

# maximum distance constraint (2.24)
def check_distance(allocation):

    for community in Community:
        shelter_name = allocation[community["name"]]
        distance = community["distances"][shelter_name]
        max_distance_community = community["maxdistance"]
        # check if distance is greater than max dist
        if (distance > max_distance_community):
            return False
        
    return True

# max shelters to be constructed/allocated constraint (2.27)
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

# count lvl 2 shelters opened (2.26)
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


# max lvl2 shelters to be constructed/allocated constraint (2.26)
def check_max_lvl2_shelters(allocation):
    return count_lvl2_shelters(allocation) <= max_lvl2_shelters

# Check all constraints
def checkConstraints(allocation):
     return (check_capacity(allocation) and 
            check_distance(allocation) and 
            check_max_shelters(allocation) and 
            check_max_lvl2_shelters(allocation))


# mutation operator
# TYPE : Random Reset
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


