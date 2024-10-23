import numpy as np

def rastrigin(x):
    return 10 * len(x) + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

def fitness(x):
    return rastrigin(x) + 1

def initialize_population(pop_size, dim, nd):
    return np.random.uniform(low=0,high=2,size=(pop_size,dim*nd)).astype(int)
    
def decode(x, lower_bound, upper_bound):
    s = 0
    for i in range(len(x)):
        s += x[len(x)-i-1] * 2**i
    return lower_bound + (upper_bound - lower_bound) / (2**len(x) - 1) * s

def roulette_wheel_selection(population, fitness_values):
    total_fitness = np.sum(fitness_values)
    selection_probs = fitness_values / total_fitness
    selected_index = np.random.choice(np.arange(len(population)), p=selection_probs)
    return population[selected_index]

def roleta(population, probs):
    i = 0
    s = probs[i]
    r = np.random.uniform()
    while s < r:
        i += 1
        s += probs[i]
    return population[i]

def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1) - 1)
    child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = 1 - individual[i] 
    return individual


def genetic_algorithm_bin(pop_size=100, dim=20, nd=8, generations=100, mutation_rate=0.1, recombination_rate=0.9, lower_bound=-10, upper_bound=10):
    population = initialize_population(pop_size, dim, nd)
    
    for g in range(generations):
        # Decodifica a população
        decoded_population = [decode(i, lower_bound, upper_bound) for i in [np.split(row, dim) for row in population]]
        # Aplica a função de aptidão
        fitness_values = np.array([fitness(ind) for ind in decoded_population]) 
        # Seleção por Roleta       
        inverse_fitness = 1 / (1 + fitness_values) 
        total_inverse_fitness = np.sum(inverse_fitness)
        probabilities = inverse_fitness / total_inverse_fitness
        selected_population = np.array([roleta(population, probabilities) for _ in range(pop_size)])

        # Cria uma nova população                
        new_population = []
        for i in range(0, pop_size, 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i+1]
            
            if np.random.rand() < recombination_rate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2
                
            new_population.append(child1)
            new_population.append(child2)


        # Aplica a mutação na nova população
        new_population = np.array([mutate(ind, mutation_rate) for ind in new_population])
        
        # Atualiza a população com a nova geração
        population = new_population        
        population = np.array(new_population)
    
    # Retorna o melhor resultado da rodada
    final_decoded_population = [decode(i, lower_bound, upper_bound) for i in [np.split(row, dim) for row in population]]
    final_fitness_values = np.array([fitness(ind) for ind in final_decoded_population])

    return np.min(final_fitness_values)



    