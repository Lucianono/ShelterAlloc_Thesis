import random
import numpy as np
import matplotlib.pyplot as plt

# List to store best fitness value from each generation
best_fitness_per_generation = []

# Updated Community Data
Community = [
    {"name": "CommA", "population": 41242, "area_per_member": 1, "distances": {"ShelA": 150, "ShelB": 250, "ShelC": 350, "ShelD": 300, "ShelE": 200, "ShelF": 400}},
    {"name": "CommB", "population": 12313, "area_per_member": 2, "distances": {"ShelA": 300, "ShelB": 1800, "ShelC": 400, "ShelD": 600, "ShelE": 220, "ShelF": 350}},
    {"name": "CommD", "population": 5123, "area_per_member": 1, "distances": {"ShelA": 500, "ShelB": 2000, "ShelC": 300, "ShelD": 400, "ShelE": 250, "ShelF": 350}},
    {"name": "CommE", "population": 2335, "area_per_member": 2, "distances": {"ShelA": 600, "ShelB": 1900, "ShelC": 300, "ShelD": 500, "ShelE": 150, "ShelF": 320}},
    {"name": "CommC", "population": 2145, "area_per_member": 1, "distances": {"ShelA": 1200, "ShelB": 450, "ShelC": 1100, "ShelD": 1300, "ShelE": 300, "ShelF": 500}}
]


# Updated Shelter Data
Level1Shelter = [
    {"name": "ShelA", "capacity": 50000, "area": 1250000, "cost_per_unit": 10},
    {"name": "ShelB", "capacity": 22000, "area": 1000000, "cost_per_unit": 20},
    {"name": "ShelE", "capacity": 5000, "area": 400000, "cost_per_unit": 10}, 
    {"name": "ShelF", "capacity": 12000, "area": 700000, "cost_per_unit": 20}, 
]

Level2Shelter = [
    {"name": "ShelC", "capacity": 1200, "area": 25000, "cost_per_unit": 20},
    {"name": "ShelD", "capacity": 1000, "area": 20000, "cost_per_unit": 10}  
]


weightDist = 0.5
weightCost = 0.5

def fitness(allocation):
    total_distance = 0
    total_cost = 0

    for community in Community:
        shelter_name = allocation[community["name"]]
        distance = community["distances"][shelter_name]
        total_distance += distance

        shelter = next(s for s in Level1Shelter + Level2Shelter if s["name"] == shelter_name)
        total_cost += shelter["cost_per_unit"] * shelter["area"]

    return weightDist * total_distance + weightCost * total_cost

def check_capacity(allocations):
    shelter_capacities = {shelter["name"]: shelter["capacity"] for shelter in Level1Shelter + Level2Shelter}
    shelter_areas = {shelter["name"]: shelter["area"] for shelter in Level1Shelter + Level2Shelter}
    used_capacity = {shelter["name"]: 0 for shelter in Level1Shelter + Level2Shelter}
    used_area = {shelter["name"]: 0 for shelter in Level1Shelter + Level2Shelter}

    for community in Community:
        shelter_name = allocations.get(community["name"])
        if shelter_name:
            population = community["population"]
            required_area = population * community["area_per_member"]

            used_capacity[shelter_name] += population
            used_area[shelter_name] += required_area

            if used_capacity[shelter_name] > shelter_capacities[shelter_name] or used_area[shelter_name] > shelter_areas[shelter_name]:
                return False

    return True

def spawn():
    allocations = {}
    for community in Community:
        shelter = random.choice(Level1Shelter)["name"]
        allocations[community["name"]] = shelter
    return allocations

def mutate(allocations):
    community_to_mutate = random.choice(list(allocations.keys()))
    current_shelter = allocations[community_to_mutate]
    
    available_shelters = [shelter["name"] for shelter in Level1Shelter + Level2Shelter if shelter["name"] != current_shelter]

    if available_shelters:
        new_shelter = random.choice(available_shelters)
        new_allocations = allocations.copy()
        new_allocations[community_to_mutate] = new_shelter
        
        return new_allocations if check_capacity(new_allocations) else allocations

    return allocations

def generate_offspring(parent1, parent2):
    offspring = {}
    for community in Community:
        shelters = {parent1[community["name"]], parent2[community["name"]]} 
        
        if shelters:
            chosen_shelter = random.choice(list(shelters))
        else:
            chosen_shelter = random.choice([shelter["name"] for shelter in Level1Shelter + Level2Shelter])

        while chosen_shelter not in [s["name"] for s in Level1Shelter + Level2Shelter]:
            chosen_shelter = random.choice([shelter["name"] for shelter in Level1Shelter + Level2Shelter])

        offspring[community["name"]] = chosen_shelter

    return offspring if check_capacity(offspring) else parent1 

def selectParent(solutions):
    sum_fitness = sum(fitness for fitness, _ in solutions)
    inv_proportions = [sum_fitness/ fitness for fitness, _ in solutions]
    sum_inv_proportions = sum(inv_proportions)
    probability = [inv_proportion / sum_inv_proportions for inv_proportion in inv_proportions]
    solution_indices = np.arange(len(solutions))

    selected_solution = np.random.choice(solution_indices, p=probability)

    return solutions[selected_solution]



def move_to_level2_shelters(allocations):
    # Initialize the level 1 population dictionary with only Level 1 shelters
    level1_population = {shelter["name"]: 0 for shelter in Level1Shelter}
    
    # Calculate the total population assigned to each Level 1 shelter
    for community, shelter in allocations.items():
        if shelter in level1_population:  # Only consider Level 1 shelters
            level1_population[shelter] += Community[next(i for i, comm in enumerate(Community) if comm["name"] == community)]["population"]

    level2_allocations = {}
    for shelter in Level2Shelter:
        capacity_remaining = shelter["capacity"]
        for community, population in level1_population.items():
            if population > 0 and capacity_remaining > 0:
                move_amount = min(population, capacity_remaining)
                level2_allocations[community] = shelter["name"]
                level1_population[community] -= move_amount  # Decrease the population left in Level 1
                capacity_remaining -= move_amount

    return level2_allocations

solutions = []
num_generations = 500
num_solutions = 200
mutation_rate = 0.5

for _ in range(num_solutions):
    solution = spawn()
    while not check_capacity(solution):
        solution = spawn()
    solutions.append(solution)

for generation in range(num_generations):

    ranked_solutions = [(fitness(sol), sol) for sol in solutions]
    ranked_solutions.sort(key=lambda x: x[0])

    new_population = []

    for i in range(num_solutions):
        mother = selectParent(ranked_solutions)[1]
        father = selectParent(ranked_solutions)[1]

        offspring = generate_offspring(mother, father)
        new_population.append(offspring)

    mutated_population = []
    for solution in new_population:
        if random.random() < mutation_rate:
            solution = mutate(solution)
        mutated_population.append((fitness(solution),solution))

    best_solutions = mutated_population + ranked_solutions
    best_solutions = sorted(best_solutions, key=lambda x: x[0])[:num_solutions] 

    print(f"=== Gen {generation} best solution ===")
    print(best_solutions[0])

    solutions = [sol[1] for sol in best_solutions]

    # Store the best fitness of this generation
    best_fitness_per_generation.append(ranked_solutions[0][0])


final_allocations = move_to_level2_shelters(solutions[0])
print("\nFinal Allocations to Level 2 Shelters:")
for comm, shelter in final_allocations.items():
    print(f"{comm} moved to {shelter}")


# Plot the fitness over generations
plt.plot(best_fitness_per_generation)
plt.xlabel('Generation')
plt.ylabel('Best Fitness')
plt.title('Best Fitness Over Generations')
plt.show()