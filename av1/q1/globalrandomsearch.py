import numpy as np
from plot_result import plot_result

def global_random_search_template(objective_function, lower_bounds, upper_bounds, epsilon=0.1, i=10000, rounds=100, max_nbh=20, earlystopping=float('inf'), maximize=True):
    final_values = []

    for round in range(rounds):
        # Inicializa a solução com um valor aleatório dentro do domínio de x
        x_opt = np.random.uniform(low=lower_bounds, high=upper_bounds)
        f_opt = objective_function(*x_opt)
        
        current_iteration = 0

        # Global Random Search loop
        while current_iteration < i:
            # Gera um novo candidato aleatoriamente
            x_cand = np.random.uniform(low=lower_bounds, high=upper_bounds, size=x_opt.shape)
            f_cand = objective_function(*x_cand)
            
            # Atualiza a solução se o novo candidato for melhor
            if (maximize and f_cand > f_opt) or (not maximize and f_cand < f_opt):
                x_opt = x_cand
                f_opt = f_cand
            
            current_iteration += 1

        # Armazena o melhor valor encontrado nesta execução
        print(f"Execution {round} completed. Final value: {f_opt:.3f}")
        final_values.append(f_opt)

    print(f"\nBest value found: {max(final_values) if maximize else min(final_values):.3f}")
    plot_result(objective_function, lower_bounds, upper_bounds, final_values, rounds)
