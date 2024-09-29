import random

Community = [
    {"name": "CommA", "population": 500, "distances": {"ShelA": 140, "ShelB": 220}},
    {"name": "CommB", "population": 400, "distances": {"ShelA": 530, "ShelB": 2100}},
    {"name": "CommC", "population": 300, "distances": {"ShelA": 1210, "ShelB": 420}}
]

Shelter = [
    {"name": "ShelA", "capacity": 800, "cost": 1000},
    {"name": "ShelB", "capacity": 800, "cost": 1000}
]

weightDist = 0.5
weightCost = 0.5

# Objective function (fitness), minimize this value
def fitness(CAAlloc, CBAlloc, CCAlloc):
    OpenShelA = int(CAAlloc == "ShelA" or CBAlloc == "ShelA" or CCAlloc == "ShelA")
    OpenShelB = int(CAAlloc == "ShelB" or CBAlloc == "ShelB" or CCAlloc == "ShelB")

    t1 = Community[0]["distances"][CAAlloc]
    t2 = Community[1]["distances"][CBAlloc]
    t3 = Community[2]["distances"][CCAlloc]

    t4 = Shelter[0]["cost"] * OpenShelA
    t5 = Shelter[1]["cost"] * OpenShelB

    return weightDist * (t1 + t2 + t3) + weightCost * (t4 + t5)

# Generate a random valid solution (shelter assignment)
def spawn():
    return (
        random.choice(Shelter)["name"],
        random.choice(Shelter)["name"],
        random.choice(Shelter)["name"]
    )

# Check if the shelter assignments respect the capacity constraints
def checkCapacity(solution):
    ShelterCapacity = [s["capacity"] for s in Shelter]

    for i in range(len(Community)):
        shelter_index = next(index for index, s in enumerate(Shelter) if s["name"] == solution[i])
        ShelterCapacity[shelter_index] -= Community[i]["population"]

        if ShelterCapacity[shelter_index] < 0:
            return False

    return True

# Mutate a random community's shelter assignment
def mutate(solution):
    community_index = random.randint(0, len(Community) - 1)
    new_shelter = random.choice(Shelter)["name"]
    
    new_solution = list(solution)
    new_solution[community_index] = new_shelter
    
    return tuple(new_solution) if checkCapacity(new_solution) else solution

# Initial population of solutions
solutions = []
for s in range(20):
    solution = spawn()
    while not checkCapacity(solution):
        solution = spawn()
    solutions.append(solution)

# Select parents based on proximity in fitness
def selectParentsByFitnessProximity(rankedsolutions):
    pairs = []
    i = 0
    while i < len(rankedsolutions) - 1:
        # Pair adjacent individuals based on their ranking
        pairs.append((rankedsolutions[i][1], rankedsolutions[i + 1][1]))
        i += 2
    return pairs

# Main evolution loop over generations
for i in range(100):
    rankedsolutions = []
    
    # Calculate fitness for each solution
    for s in solutions:
        rankedsolutions.append((fitness(s[0], s[1], s[2]), s))

    # Sort solutions by fitness (lower is better)
    rankedsolutions.sort(key=lambda x: x[0])

    # Select pairs of parents with similar fitness
    pairs = selectParentsByFitnessProximity(rankedsolutions)

    # Generate the next generation
    newPopulation = []
    for mother, father in pairs:
        # Keep the parents in the new population
        newPopulation.append(mother)
        newPopulation.append(father)

        # Crossover: offspring inherit randomly from either parent
        offspringA = tuple(random.choice([mother[i], father[i]]) for i in range(3))
        if checkCapacity(offspringA):
            newPopulation.append(offspringA)
        
        offspringB = tuple(random.choice([mother[i], father[i]]) for i in range(3))
        if checkCapacity(offspringB):
            newPopulation.append(offspringB)

    # Ensure population size remains constant by adding random old solutions if necessary
    while len(newPopulation) < len(solutions):
        newPopulation.append(random.choice(solutions))

    # Apply mutation with a fixed probability
    mutationRate = 0.1
    mutatedPopulation = []
    for solution in newPopulation:
        if random.random() < mutationRate:
            solution = mutate(solution)
        mutatedPopulation.append(solution)

    # Update solutions for the next generation
    solutions = mutatedPopulation[:20]

    # Print the best solution from this generation
    print(f"=== Gen {i} best solutions ===")
    print(rankedsolutions[0])
