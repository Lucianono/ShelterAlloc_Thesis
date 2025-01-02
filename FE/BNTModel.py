# =======================
# the Official Function for Bilevel No Transfer model
# =======================

import random
import numpy as np
import pandas as pd
import os

# =======================
# IMPORT DATA
# get data and parameters from excel
Community_data = pd.read_excel( os.path.join(os.getcwd(), "commData.xlsx") ).fillna("")
Shelter_data = pd.read_excel( os.path.join(os.getcwd(), "shelData.xlsx") ).fillna("")
Distances_data = pd.read_excel( os.path.join(os.getcwd(), "distance_matrix.xlsx") ).fillna("")

# simulation of area required per individual (meters squared), maximum no. of level 2 shelters
area_per_individual = 0.01
max_lvl2_shelters = 22
max_shelters = 22

solutions = []
num_generations = 100
num_solutions = 20
mutation_rate = 0.5

weight_dist = 0.5
weight_cost = 0.5

# list of shelters with area1 and cost1 (area and cost as level 1 shelter), area 2 and cost2 (area and cost as level 2 shelter) 
Shelters = []
for row in Shelter_data.itertuples(index=False):
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
for row in Community_data.itertuples(index=False):
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

    # check if there exists population * areaPerIndiv <= shelter area 
    failing_communities = []
    for community in Community:
        if not (
            any(shelter["area1"] >= area_per_individual * community["population"] for shelter in Shelters) or
            any(shelter["area2"] >= area_per_individual * community["population"] for shelter in Shelters)
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

    if total_population > ((top_area2_sum + top_area1_sum) / area_per_individual):
        print(f"Total capacity of shelters available are less than the total affected population. Shelters has lower than expected capacity")
        print(f"Total capacity of shelters :  {(top_area2_sum + top_area1_sum) / area_per_individual }" )
        print(f"Total population : {total_population}")
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

# Function to read community coordinates from the Excel file
def read_community_coordinates():
    community_coords_df = pd.read_excel("commData.xlsx")
    return {row["Name"]: {"Latitude": row["yDegrees"], "Longitude": row["xDegrees"]} 
            for _, row in community_coords_df.iterrows()}

# Function to read shelter coordinates from the Excel file
def read_shelter_coordinates():
    shelter_coords_df = pd.read_excel("shelData.xlsx")
    return {row["Name"]: {"Latitude": row["yDegrees"], "Longitude": row["xDegrees"]} 
            for _, row in shelter_coords_df.iterrows()}


def export_to_excel(allocation, community_coords, shelter_coords):
    data = []
    
    for community in Community:
        shelter_name = allocation[community["name"]]
        population = community["population"]
        
        # Get coordinates from the community coordinates dataframe
        community_lat = community_coords.get(community["name"], {}).get("Latitude", None)
        community_lon = community_coords.get(community["name"], {}).get("Longitude", None)
        
        # Get coordinates from the shelter coordinates dataframe
        shelter_lat = shelter_coords.get(shelter_name, {}).get("Latitude", None)
        shelter_lon = shelter_coords.get(shelter_name, {}).get("Longitude", None)
        
        # Calculate used area and shelter level
        shelter_areas_lvl1 = {shelter["name"]: shelter["area1"] for shelter in Shelters}
        shelter_areas_lvl2 = {shelter["name"]: shelter["area2"] for shelter in Shelters}
        
        used_area = population * area_per_individual
        if used_area <= shelter_areas_lvl1[shelter_name]:
            level = "Level 1"
        else:
            level = "Level 2"
        
        # Append data
        data.append({
            "Community Name": community["name"],
            "Community Latitude": community_lat,
            "Community Longitude": community_lon,
            "Shelter Assigned": shelter_name,
            "Shelter Latitude": shelter_lat,
            "Shelter Longitude": shelter_lon,
            "Population": population,
            "Area Used (m²)": used_area,
            "Shelter Level": level
        })
    
    # Create a DataFrame and export to Excel
    df = pd.DataFrame(data)
    output_file = os.path.join(os.getcwd(), "allocation_results.xlsx")
    df.to_excel(output_file, index=False)

    print(f"Allocation results saved to {output_file}")

community_coords = read_community_coordinates()
shelter_coords = read_shelter_coordinates()


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
for _ in range(num_solutions):
    solution = spawn()
    while not checkConstraints(solution):
        infeasibility_ctr += 1
        # warning and halting
        if infeasibility_ctr >= 100000:
            print ("WARNING: 100000 infeasible solutions are generated. Program stopping.")
            exit()
        elif infeasibility_ctr % 10000 == 0:
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

export_to_excel(best_allocation, community_coords, shelter_coords)


