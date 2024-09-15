import numpy as np
from plot_result import plot_result

def hill_climbing_template(objective_function, lower_bounds, upper_bounds, epsilon=0.1, i=10000, rounds=100, max_nbh=20, earlystopping=float('inf'), maximize=True):
  def perturb(x, epsilon):
    return np.random.uniform(low=x-epsilon, high=x+epsilon, size=x.shape)

  final_values = []

  for round in range(rounds):
    # Inicializa a solução no limite inferior do domínio
    x_opt = np.array(lower_bounds)
    f_opt = objective_function(*x_opt)

    current_iteration = 0
    has_improvement = True

    # Hill Climbing loop
    while current_iteration < i and has_improvement:
      has_improvement = False
      for _ in range(max_nbh):
        # Pertubação
        x_cand = perturb(x_opt, epsilon)
        # Restrição de caixa
        x_cand = np.clip(x_cand, lower_bounds, upper_bounds)
        f_cand = objective_function(*x_cand)

        if (maximize and f_cand > f_opt) or (not maximize and f_cand < f_opt):
          x_opt = x_cand
          f_opt = f_cand
          has_improvement = True
          break
        current_iteration += 1

    # Armazena o melhor valor encontrado nesta execução
    print(f"Execution {round} completed. Final value: {f_opt:.3f}")
    final_values.append(f_opt)

  print(f"\nBest value found: {max(final_values) if maximize else min(final_values):.3f}")
  plot_result(objective_function, lower_bounds, upper_bounds, final_values, rounds)


