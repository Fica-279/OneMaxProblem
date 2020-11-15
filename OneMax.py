# This code solves One Max problem. It generates random sequence of 0s and 1s.
# The goal is to find the sequence of all 1s using genetic algorithm.

import random
import decimal

n = 50  # number of genes
populationSize = 500  # size of the population, stays the same the entire time
numberOfGenerations = 50  # max number of generations
mutationProbability = 0.15  # probability of mutation
crossingProbability = 0.75  # probability of crossing
survivalProbability = 0.05  # probability of not selecting individuals with lower fitness to be removed
maxMutationPercentage = 0.20  # max percentages of genes that can be mutated

population = []  # list that stores current population
temp_population = []  # help list that stores fitness for current population

end = False

# initialize 0. population
for i in range(populationSize):
    x = ""
    for j in range(n):
        x += str(random.randint(0, 1))
    population.append(x)


#  calculate the fitness of one individual by counting number of 1s
def fitness(individual):
    result = 0
    for i in range(0, len(individual)):
        if individual[i] == '1':
            result += 1
    return result


# variable that stores the average fitness of the entire population
average = 0.5


# loop for every generation
for gen in range(1, numberOfGenerations + 1):
    average = 0.0
    temp_population = []
    print("GENERATION " + str(gen))
    for i in range(0, populationSize):
        #  calculates fitness for every individual and stores it in temp_population
        individual = population[i]
        fit = fitness(individual)
        # prints if it finds 100% fitness
        if fit == n:
            print("SOLUTION FOUND")
            print("individual: " + individual + " | " + str(fit))
            print("GENERATION: " + str(gen))
            end = True
            break
        print("individual: " + individual + " | " + str(fit))
        temp_population.append(fit)
        average += fit / n
    # stops if it finds 100% fitness
    if end:
        break
    temp_population.sort()
    print("average = " + str(average / populationSize) + " %")
    #  if fitness of the individual is lower than the one that is in the middle of sorted temp_population
    #  we remove that individual with given percentage, if it is higher we leave it in the population
    for i in range(0, populationSize):
        individual = population[i]
        fit = fitness(individual)
        if temp_population.index(fit) < (populationSize / 2) and temp_population[temp_population.index(fit)] != \
                temp_population[-2] and survivalProbability <= float(decimal.Decimal(random.randrange(0, 100)) / 100):
            population[i] = 'x'
    i = 0
    # removing selected individuals
    while i < len(population):
        if population[i] == 'x':
            population.remove(population[i])
        else:
            i += 1

    # crossing while we don't get the entire new population
    i = len(population)
    while i < populationSize:
        # if crossing probability is lower, we add completely new gene material to the population
        if crossingProbability >= float(decimal.Decimal(random.randrange(0, 100)) / 100):
            x1 = random.randint(0, len(population) - 1)
            x2 = (x1 + (random.randint(1, len(population) - 1))) % len(population)
            individual1 = population[x1]
            individual2 = population[x2]
            numberOfChanges = random.randint(1, n - 1)
            population.append(individual1[:numberOfChanges] + individual2[numberOfChanges:])
            i += 1
        else:
            x = ""
            for j in range(n):
                x += str(random.randint(0, 1))
            population.append(x)
            i += 1
        # for every crossing or new individual there is a chance of mutation for randomly selected individual
        if mutationProbability >= float(decimal.Decimal(random.randrange(0, 100)) / 100):
            x1 = random.randint(0, len(population) - 1)
            individual1 = population[x1]
            numberOfChanges = random.randint(1, int(n * maxMutationPercentage))
            # randomly select a gene to be mutated
            for j in range(numberOfChanges):
                index = random.randint(0, n - 1)
                individual1 = individual1[:index] + str((int(individual1[index]) + 1) % 2) + individual1[index + 1:]
            population[x1] = individual1
