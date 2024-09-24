import random

# Community now includes area_per_member
Community = [
    {"name": "CommA", "population": 500, "area_per_member": 2, "distances": {"ShelA": 140, "ShelB": 220, "ShelC": 300, "ShelD": 250}},
    {"name": "CommB", "population": 400, "area_per_member": 2.5, "distances": {"ShelA": 530, "ShelB": 2100, "ShelC": 450, "ShelD": 500}},
    {"name": "CommC", "population": 300, "area_per_member": 1.8, "distances": {"ShelA": 1210, "ShelB": 420, "ShelC": 1100, "ShelD": 1200}}
]

# More shelters can be added here
Level1Shelter = [
    {"name": "ShelA", "capacity": 800, "area": 2000, "cost_per_person": 1000},
    {"name": "ShelB", "capacity": 600, "area": 1800, "cost_per_person": 900}  
]

Level2Shelter = [
    {"name": "ShelC", "capacity": 800, "area": 2500, "cost_per_person": 1500},
    {"name": "ShelD", "capacity": 700, "area": 2200, "cost_per_person": 1300}  
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
        total_cost += shelter["cost_per_person"] * community["population"]

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
num_generations = 100
num_solutions = 20

for _ in range(num_solutions):
    solution = spawn()
    while not check_capacity(solution):
        solution = spawn()
    solutions.append(solution)

for generation in range(num_generations):
    ranked_solutions = [(fitness(sol), sol) for sol in solutions]
    ranked_solutions.sort(key=lambda x: x[0])

    print(f"=== Gen {generation} best solution ===")
    print(ranked_solutions[0])

    new_population = []

    new_population.extend([ranked_solutions[0][1], ranked_solutions[1][1]])

    for i in range(2, len(ranked_solutions) - 1, 2):
        mother = ranked_solutions[i][1]
        father = ranked_solutions[i + 1][1]

        offspring = generate_offspring(mother, father)
        new_population.append(offspring)

    mutated_population = []
    for solution in new_population:
        if random.random() < 0.1:
            solution = mutate(solution)
        mutated_population.append(solution)

    solutions = mutated_population[:num_solutions]

final_allocations = move_to_level2_shelters(solutions[0])
print("\nFinal Allocations to Level 2 Shelters:")
for comm, shelter in final_allocations.items():
    print(f"{comm} moved to {shelter}")