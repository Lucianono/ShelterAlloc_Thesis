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

# Objective function, also the fitness
# minimize fitness
def fitness(CAAlloc, CBAlloc, CCAlloc):
    OpenShelA = int(CAAlloc == "ShelA" or CBAlloc == "ShelA" or CCAlloc == "ShelA")
    OpenShelB = int(CAAlloc == "ShelB" or CBAlloc == "ShelB" or CCAlloc == "ShelB")

    t1 = Community[0]["distances"][CAAlloc]
    t2 = Community[1]["distances"][CBAlloc]
    t3 = Community[2]["distances"][CCAlloc]

    t4 = Shelter[0]["cost"] * OpenShelA
    t5 = Shelter[1]["cost"] * OpenShelB

    return weightDist * (t1 + t2 + t3) + weightCost * (t4 + t5)

# kill solution if constraint fail, then spawn random solution
def spawn():
    return (
        random.choice(Shelter)["name"],
        random.choice(Shelter)["name"],
        random.choice(Shelter)["name"]
    )

# check if solution is feasible in capacity of shelter
# constraint for capacity
def checkCapacity(solution):
    ShelterCapacity = [s["capacity"] for s in Shelter]

    for i in range(len(Community)):
        shelter_index = next(index for index, s in enumerate(Shelter) if s["name"] == solution[i])
        ShelterCapacity[shelter_index] -= Community[i]["population"]

        if ShelterCapacity[shelter_index] < 0:
            return False

    return True

# Mutation function
def mutate(solution):
    # Pick a random community to mutate
    community_index = random.randint(0, len(Community) - 1)
    new_shelter = random.choice(Shelter)["name"]
    
    # Create a new mutated solution
    new_solution = list(solution)
    new_solution[community_index] = new_shelter
    
    return tuple(new_solution) if checkCapacity(new_solution) else solution

# initial population
solutions = []
for s in range(20):
    solution = spawn()
    while not checkCapacity(solution):
        solution = spawn()
    solutions.append(solution)

# generations
for i in range(100):
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append((fitness(s[0], s[1], s[2]), s))

    
    rankedsolutions.sort(key=lambda x: x[0])

    # Creating new population
    newPopulation = []
    while len(newPopulation) < len(solutions):
        mother = random.choice(solutions)
        father = random.choice(solutions)

        offspringA = (mother[0], father[1], mother[2])
        if checkCapacity(offspringA):
            newPopulation.append(offspringA)

        offspringB = (father[0], mother[1], father[2])
        if checkCapacity(offspringB):
            newPopulation.append(offspringB)

    # check new generation has same no. of solutions
    while len(newPopulation) < len(solutions):
        newPopulation.append(random.choice(solutions))

    # Apply mutation
    mutationRate = 0.05  # Probability of mutation
    mutatedPopulation = []
    for solution in newPopulation:
        if random.random() < mutationRate:
            solution = mutate(solution)
        mutatedPopulation.append(solution)

    solutions = mutatedPopulation[:20]

    print(f"=== Gen {i} best solutions ===")
    print(rankedsolutions[0])