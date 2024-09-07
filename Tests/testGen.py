import random

Community = [
    {"name": "CommA", "population": 500, "distances": {"ShelA": 140, "ShelB": 220}},
    {"name": "CommB", "population": 400, "distances": {"ShelA": 530, "ShelB": 2100}},
    {"name": "CommC", "population": 300, "distances": {"ShelA": 1210, "ShelB": 420}}
]

Shelter = [
    {"name": "ShelA", "capacity": 10000, "cost": 500},
    {"name": "ShelB", "capacity": 10000, "cost": 500}
]

weightDist = 0.5
weightCost = 0.5

# objective function, also the fitness
# minimize fitness
def fitness(CAAlloc,CBAlloc,CCAlloc):
    OpenShelA = 0
    OpenShelB = 0

    t1 = Community[0]["distances"][CAAlloc]
    t2 = Community[1]["distances"][CBAlloc]
    t3 = Community[2]["distances"][CCAlloc]

    if(CAAlloc == "ShelA" or CBAlloc == "ShelA" or CCAlloc == "ShelA"):
        OpenShelA = 1
    if(CAAlloc == "ShelB" or CBAlloc == "ShelB" or CCAlloc == "ShelB"):
        OpenShelB = 1

    t4 = Shelter[0]["cost"] * OpenShelA
    t5 = Shelter[1]["cost"] * OpenShelB

    return weightDist*(t1+t2+t3) + weightCost*(t4+t5)

# kill solution if constraint fail, then spawn random solution
def spawn():
    return (random.choice(Shelter),
            random.choice(Shelter),
            random.choice(Shelter) )

# check if solution is feasible in capacity of shelter
def checkCapacity(solution):
    ShelterCapacity = []

    for i in Shelter:
        ShelterCapacity.append(i["capacity"])

    for i in len(Community):
        ShelterCapacity[solution[i]] - Community[i]["population"]


    

    Community[0]["population"]



    solution[0]["capacity"] + solution[0]["capacity"] + solution[0]["capacity"]



#initial population
solutions = []
for s in range(20):
    solutions.append (
        (random.choice(Shelter),
        random.choice(Shelter),
        random.choice(Shelter))

    )

#generations
for i in range(100):

    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append( (fitness(s[0]["name"],s[1]["name"],s[2]["name"]),s) )

    for _ in range(len(solutions) // 2):
        # selecting parents
        mother = random.choice(solutions)
        father = random.choice(solutions)

        # crossover
        offspringA = (mother[0],
                      father[1],
                      mother[2])
        offspringB = (father[0],
                      mother[1],
                      father[2])
        
        rankedsolutions.append( (fitness(offspringA[0]["name"],offspringA[1]["name"],offspringA[2]["name"]),offspringA) )
        rankedsolutions.append( (fitness(offspringB[0]["name"],offspringB[1]["name"],offspringB[2]["name"]),offspringB) )

    # ranking population
    rankedsolutions.sort(key=lambda x: x[0])

    # getting ready new population for next generation
    bestsolutions = rankedsolutions[:20]
    newGen = []
    for j in bestsolutions:
        newGen.append(j[1])
    solutions = newGen

    print(f"=== Gen {i} best solutions ===")
    print(bestsolutions[0])

