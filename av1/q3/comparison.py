import numpy as np
import pandas as pd
from genetic_canon import genetic_algorithm_bin
from genetic_float import genetic_algorithm_float

# Hyperparametros
pop_size = 100
dim = 20
nd = 8
generations = 100
mutation_rate = 0.1
recombination_rate = 0.9
lower_bound = -10
upper_bound = 10
tournament_size = 10
distribution_index = 1


results_bin = []
results_float = []
for round_num in range(100):
    best_fitness_bin = genetic_algorithm_bin(
        pop_size=pop_size,
        dim=dim,
        nd=nd,
        generations=generations,
        mutation_rate=mutation_rate,
        recombination_rate=recombination_rate,
        lower_bound=lower_bound,
        upper_bound=upper_bound
    )
    results_bin.append(best_fitness_bin)
    
    best_fitness_float = genetic_algorithm_float(
        pop_size=pop_size,
        dim=dim,
        generations=generations,
        mutation_rate=mutation_rate,
        recombination_rate=recombination_rate,
        tournament_size=tournament_size,
        distribution_index=distribution_index,
        lower_bound=lower_bound,
        upper_bound=upper_bound
    )
    results_float.append(best_fitness_float)
    
    print(f'Rodada {round_num + 1} concluida')

results_bin = np.array(results_bin)
results_float = np.array(results_float)

min_bin = np.min(results_bin)
max_bin = np.max(results_bin)
mean_bin = np.mean(results_bin)
std_bin = np.std(results_bin)

min_float = np.min(results_float)
max_float = np.max(results_float)
mean_float = np.mean(results_float)
std_float = np.std(results_float)

# Create DataFrames for results
df_results = pd.DataFrame({
    'Algoritmo': ['Binary Genetic Algorithm', 'Float Genetic Algorithm'],
    'Min Fitness': [min_bin, min_float],
    'Max Fitness': [max_bin, max_float],
    'Mean Fitness': [mean_bin, mean_float],
    'Std Fitness': [std_bin, std_float]
})

df_results = df_results.round(3)

# Display the results
print("\nGenetic Algorithm Results Summary:")
print(df_results)