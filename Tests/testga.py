import random
import matplotlib.pyplot as plt # type: ignore

#objective function
def foo(x,y,z):
    return x**3 + y**3 + z**3 - 100

#fitness function

def fitness(x,y,z):
    ans = foo(x,y,z)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)
    
#initial population
solutions = []
for s in range(1000):
    solutions.append (
        (random.uniform(0,10000),
        random.uniform(0,10000),
        random.uniform(0,10000))

    )

# To store fitness history
fitness_history = []

# To store best x, y, z values history
x_history = []
y_history = []
z_history = []

#generations
for i in range(2000):

    
    rankedsolutions = []
    for _ in range(len(solutions) // 2):
        #selecting parents
        mother = random.choice(solutions)
        father = random.choice(solutions)

        #crossover
        offspringA = (mother[0] * random.uniform(0.99,1.01),
                      father[1] * random.uniform(0.99,1.01),
                      mother[2] * random.uniform(0.99,1.01))
        offspringB = (father[0] * random.uniform(0.99,1.01),
                      mother[1] * random.uniform(0.99,1.01),
                      father[2] * random.uniform(0.99,1.01))
        
        rankedsolutions.append( (fitness(offspringA[0],offspringA[1],offspringA[2]),offspringA) )
        rankedsolutions.append( (fitness(offspringB[0],offspringB[1],offspringB[2]),offspringB) )


    #ranking population
    for s in solutions:
        rankedsolutions.append( (fitness(s[0],s[1],s[2]),s) )
    rankedsolutions.sort(reverse=True)

    bestsolutions = rankedsolutions[:100]
    newGen = []
    for j in bestsolutions:
        newGen.append(j[1])

    # Save best x, y, z for this generation
    best_x = bestsolutions[0][1][0]
    best_y = bestsolutions[0][1][1]
    best_z = bestsolutions[0][1][2]
    
    x_history.append(best_x)
    y_history.append(best_y)
    z_history.append(best_z)

    print(f"=== Gen {i} best solutions ===")
    print(bestsolutions[0])
    
    # Save best fitness score for this generation
    best_fitness = bestsolutions[0][0]
    fitness_history.append(best_fitness)

    # break if certain fitness is acheived
    if(bestsolutions[0][0] > 2000):
        print(foo(bestsolutions[0][1][0],
                  bestsolutions[0][1][1],
                  bestsolutions[0][1][2]) + 100)
        break

    solutions = newGen


# Plot x, y, z over generations
plt.plot(x_history, label='x')
plt.plot(y_history, label='y')
plt.plot(z_history, label='z')
plt.title('Best x, y, z Values Over Generations')
plt.xlabel('Generations')
plt.ylabel('Values of x, y, z')
plt.legend()
plt.show()