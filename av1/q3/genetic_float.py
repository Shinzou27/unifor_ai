import numpy as np

def rastrigin(x):
    return 10 * len(x) + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

def fitness(x):
    return rastrigin(x) + 1

def initialize_population(pop_size, dim, lower_bound, upper_bound):
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dim))

def tournament_selection(population, fitness_values, tournament_size):
    selected = []
    for _ in range(len(population)):
        indices = np.random.choice(len(population), tournament_size, replace=False)
        tournament_fitness = fitness_values[indices]
        winner_index = indices[np.argmin(tournament_fitness)]
        selected.append(population[winner_index])
    return np.array(selected)

def sbx_crossover(parent1, parent2, lower_bound, upper_bound, distribution_index):
    u = np.random.uniform(size=len(parent1))
    beta = np.where(u <= 0.5, (2 * u)**(1 / (distribution_index + 1)), (1 / (2 * (1 - u)))**(1 / (distribution_index + 1)))
    child1 = 0.5 * ((1 + beta) * parent1 + (1 - beta) * parent2)
    child2 = 0.5 * ((1 - beta) * parent1 + (1 + beta) * parent2)
    
    # Clip children to bounds
    child1 = np.clip(child1, lower_bound, upper_bound)
    child2 = np.clip(child2, lower_bound, upper_bound)
    
    return child1, child2

def gaussian_mutation(individual, mutation_rate, lower_bound, upper_bound, sigma=0.1):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            mutation = np.random.normal(0, sigma)
            individual[i] += mutation
            individual[i] = np.clip(individual[i], lower_bound, upper_bound)
    return individual

def genetic_algorithm_float(pop_size=100, dim=20, generations=100, mutation_rate=0.1, recombination_rate=0.9, tournament_size=10, distribution_index=1, lower_bound=-10, upper_bound=10):
    population = initialize_population(pop_size, dim, lower_bound, upper_bound)
    
    for g in range(generations):
        # Aplica a função de aptidão
        fitness_values = np.array([fitness(ind) for ind in population])
        
        # Seleção por Torneio
        selected_population = tournament_selection(population, fitness_values, tournament_size)
        
        # Cria uma nova população
        new_population = []
        for i in range(0, pop_size, 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i+1]
            
            if np.random.rand() < recombination_rate:
                child1, child2 = sbx_crossover(parent1, parent2, lower_bound, upper_bound, distribution_index)
            else:
                child1, child2 = parent1, parent2
                
            new_population.append(child1)
            new_population.append(child2)
        
        # Aplica a mutação na nova população
        new_population = np.array([gaussian_mutation(ind, mutation_rate, lower_bound, upper_bound) for ind in new_population])
        
        # Atualiza a população com a nova geração
        population = new_population
    
    # Avalia a população final
    final_fitness_values = np.array([fitness(ind) for ind in population])
    return np.min(final_fitness_values)


