import numpy as np
import matplotlib.pyplot as plt

def hill_climbing(objective_function, lower_bounds, upper_bounds, epsilon=0.1, i=1000, num_runs=100, persistLimit=100, maximize=False):
    f_values = []
    for _ in range(num_runs):
        current_solution = np.array([lower_bounds[0], lower_bounds[1]])
        current_value = objective_function(*current_solution)
        persistCount = 0
        for _ in range(i):
            candidate = current_solution + np.random.uniform(-epsilon, epsilon, size=current_solution.shape)
            candidate = np.maximum(lower_bounds, np.minimum(candidate, upper_bounds))
            candidate_value = objective_function(*candidate)
            if (maximize and candidate_value > current_value) or (not maximize and candidate_value < current_value):
                current_solution = candidate
                current_value = candidate_value
                persistCount = 0
            else:
                persistCount += 1
            if persistCount >= persistLimit:
                break
        f_values.append(current_value)
    plot_results(f_values)
    return f_values

def plot_results(f_values):
    plt.figure(figsize=(15, 9))
    plt.plot(f_values, marker='o', linestyle='-', color='b')
    plt.title('Hill Climbing AV1')
    plt.xlabel('Rodadas')
    plt.ylabel('Valor obtido')
    plt.grid(True)
    plt.show()


def hill_climbing_template(objective_function, lower_bounds, upper_bounds, epsilon=0.1, i=10000, rounds = 100, persistLimit=100, maximize=True):
    def perturb(x, epsilon):
        return np.random.uniform(low=x-epsilon, high=x+epsilon, size=x.shape)

    # Parâmetros do algoritmo de Hill Climbing
    i = 10000
    max_viz = 20
    final_values = []

    for round in range(rounds):
        values = []
        # Inicializa a solução com o limite inferior do domínio de x
        x_opt = np.array(lower_bounds)  # Ponto inicial
        f_opt = objective_function(*x_opt)
        
        melhoria = True
        current_iteration = 0

        # Hill Climbing
        while current_iteration < i and melhoria:
            melhoria = False
            for _ in range(max_viz):
                x_cand = perturb(x_opt, epsilon)
                f_cand = objective_function(*x_cand)
                if (maximize and f_cand > f_opt) or (not maximize and f_cand < f_opt):
                    x_opt = x_cand
                    f_opt = f_cand
                    values.append(f_opt)
                    melhoria = True
                    break
            current_iteration += 1
        # Armazena o melhor valor encontrado nesta execução
        print(f"Execução {round} concluída. Valor final: {f_opt}")
        print(*x_opt)
        final_values.append(f_opt)

    # Plotagem dos valores finais de cada execução
    x_axis = np.linspace(1, 100, 100)
    plt.plot(x_axis, final_values)
    plt.show()