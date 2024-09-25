import random

Community = [
    {"name": "CommA", "population": 500, "distances": {"ShelA": 140, "ShelB": 220}},
    {"name": "CommB", "population": 400, "distances": {"ShelA": 530, "ShelB": 2100}},
    {"name": "CommC", "population": 300, "distances": {"ShelA": 1210, "ShelB": 420}}
]
Level1Shelter = [
    {"name": "ShelA", "capacity": 800, "cost": 1000},
]

Level2Shelter = [
    {"name": "ShelB", "capacity": 800, "cost": 1000},
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
        total_cost += 1000

    return weightDist * total_distance + weightCost * total_cost

def spawn():
    allocations = {}
    for community in Community:
        shelter = random.choice(Level1Shelter)["name"]
        allocations[community["name"]] = shelter
    return allocations

def check_capacity(allocations):
    shelter_capacities = {shelter["name"]: shelter["capacity"] for shelter in Level1Shelter}

    for community in Community:
        shelter_name = allocations.get(community["name"])
        if shelter_name and community["population"] > shelter_capacities[shelter_name]:
            return False

    return True

def mutate(allocations):
    community_to_mutate = random.choice(list(allocations.keys()))
    current_shelter = allocations[community_to_mutate]
    
    available_shelters = [shelter["name"] for shelter in Level1Shelter if shelter["name"] != current_shelter]

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
            chosen_shelter = random.choice([shelter["name"] for shelter in Level1Shelter]) 

        while chosen_shelter not in [s["name"] for s in Level1Shelter]:
            chosen_shelter = random.choice([shelter["name"] for shelter in Level1Shelter])

        offspring[community["name"]] = chosen_shelter

    return offspring if check_capacity(offspring) else parent1 

def move_to_level2_shelters(allocations):
    level1_population = {shelter["name"]: 0 for shelter in Level1Shelter}
    
    for community, shelter in allocations.items():
        level1_population[shelter] += Community[next(i for i, comm in enumerate(Community) if comm["name"] == community)]["population"]

    level2_allocations = {}
    for shelter in Level2Shelter:
        capacity_remaining = shelter["capacity"]
        for community, population in level1_population.items():
            if population > 0 and capacity_remaining > 0:
                move_amount = min(population, capacity_remaining)
                level2_allocations[community] = shelter["name"]
                level1_population[community] -= move_amount
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
