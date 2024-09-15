import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def local_random_search_template(objective_function, lower_bounds, upper_bounds, epsilon=0.1, i=10000, rounds=100, earlystopping=float('inf'), maximize=True):
  def perturb(x, epsilon):
    return np.random.uniform(low=x-epsilon, high=x+epsilon, size=x.shape)

  final_values = []

  for round in range(rounds):
    # Inicializa a solução com um valor aleatório dentro do domínio de x
    x_opt = np.random.uniform(low=lower_bounds, high=upper_bounds)
    f_opt = objective_function(*x_opt)
    
    current_iteration = 0
    no_improvement_counter = 0

    # LRS loop
    while current_iteration < i and no_improvement_counter < earlystopping:
      # Pertubação
      x_cand = perturb(x_opt, epsilon)  
      # Restrição de caixa          
      x_cand = np.clip(x_cand, lower_bounds, upper_bounds)
      f_cand = objective_function(*x_cand)
      
      if (maximize and f_cand > f_opt) or (not maximize and f_cand < f_opt):
        x_opt = x_cand
        f_opt = f_cand
        no_improvement_counter = 0
      else:
        no_improvement_counter += 1
      current_iteration += 1

    # Armazena o melhor valor encontrado nesta execução
    print(f"Execution {round} completed. Final value: {f_opt:.3f}")
    final_values.append(f_opt)

  print(f"\nBest value found: {max(final_values) if maximize else min(final_values):.3f}")

  # Plotagem dos valores finais de cada execução
  x_axis = np.arange(1, rounds + 1)
  plt.plot(x_axis, final_values)

  # Tabela de frequência por intervalo
  final_values = np.round(final_values, 3)

  min_val = int(np.floor(min(final_values)))
  max_val = int(np.ceil(max(final_values)))
  bins = np.arange(min_val, max_val + 2, 1) 
  counts, bin_edges = np.histogram(final_values, bins=bins)
  df = pd.DataFrame({
      'Intervalo': [f'{edge}-{edge+1}' for edge in bin_edges[:-1]],
      'Ocorrências': counts
  })
  print("\nFrequência das Soluções Encontradas por Intervalo:")
  print(df)
    
  plt.show()