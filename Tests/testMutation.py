import random

Community = [
    {"name": "CommA", "population": 500, "distances": {"ShelA": 140, "ShelB": 220}},
    {"name": "CommB", "population": 400, "distances": {"ShelA": 530, "ShelB": 2100}},
    {"name": "CommC", "population": 300, "distances": {"ShelA": 1210, "ShelB": 420}},
    {"name": "CommD", "population": 200, "distances": {"ShelA": 620, "ShelB": 320}}
]

Shelter = [
    {"name": "ShelA", "capacity": 800, "cost": 1000},
    {"name": "ShelB", "capacity": 800, "cost": 1000}
]

weightDist = 0.5
weightCost = 0.5

# Objective function, also the fitness
# minimize fitness
def fitness(solution):
    # Check if shelters are open
    open_shelters = {s["name"]: False for s in Shelter}
    
    total_distance = 0
    total_cost = 0

    # Calculate total distance and mark shelters as open
    for i, community in enumerate(Community):
        assigned_shelter = solution[i]
        total_distance += community["distances"][assigned_shelter]
        open_shelters[assigned_shelter] = True

    # Calculate total cost
    for shelter in Shelter:
        if open_shelters[shelter["name"]]:
            total_cost += shelter["cost"]

    return weightDist * total_distance + weightCost * total_cost

def spawn():
    return tuple(random.choice(Shelter)["name"] for _ in Community)

def checkCapacity(solution):
    ShelterCapacity = {s["name"]: s["capacity"] for s in Shelter}

    
    for i, community in enumerate(Community):
        ShelterCapacity[solution[i]] -= community["population"]

    # Return False if any shelter exceeds capacity
    return all(capacity >= 0 for capacity in ShelterCapacity.values())

# Mutation function
def mutate(solution):
    # random community to mutate
    community_index = random.randint(0, len(Community) - 1)
    new_shelter = random.choice(Shelter)["name"]
    
    # new mutated solution
    new_solution = list(solution)
    new_solution[community_index] = new_shelter
    
    return tuple(new_solution) if checkCapacity(new_solution) else solution

# Initial population
solutions = []
for _ in range(20):
    solution = spawn()
    while not checkCapacity(solution):
        solution = spawn()
    solutions.append(solution)

# Generations
for generation in range(100):
    ranked_solutions = [(fitness(s), s) for s in solutions]
    ranked_solutions.sort(key=lambda x: x[0])

    def selectParent(ranked_solutions):
        # Choose a parent based on smash
        return random.choice([s[1] for s in ranked_solutions[:5]])

    # Creating new population
    new_population = []
    while len(new_population) < len(solutions):
        mother = selectParent(ranked_solutions)
        father = selectParent(ranked_solutions)

        offspring_a = tuple(random.choice([mother[i], father[i]]) for i in range(len(Community)))
        if checkCapacity(offspring_a):
            new_population.append(offspring_a)

        offspring_b = tuple(random.choice([mother[i], father[i]]) for i in range(len(Community)))
        if checkCapacity(offspring_b):
            new_population.append(offspring_b)

    # check population has the same number of solutions
    while len(new_population) < len(solutions):
        new_population.append(random.choice(solutions))

    # mutation
    mutation_rate = 0.1  # Probability of mutation
    mutated_population = []
    for solution in new_population:
        if random.random() < mutation_rate:
            solution = mutate(solution)
        mutated_population.append(solution)

    solutions = mutated_population[:20]

    # Print best solution
    print(f"=== Generation {generation} best solution ===")
    print(ranked_solutions[0])
