import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

def plot_result(obj_func, lower_bounds, upper_bounds, final_values, rounds):
  # Create a grid of points in the domain of the function
  x1 = np.linspace(lower_bounds[0], upper_bounds[0], 100)
  x2 = np.linspace(lower_bounds[1], upper_bounds[1], 100)
  X1, X2 = np.meshgrid(x1, x2)
  Z = obj_func(X1, X2)

  # Create a 3D plot
  fig = plt.figure(figsize=(12, 6))

  # 3D Surface Plot
  ax1 = fig.add_subplot(121, projection='3d')
  ax1.plot_surface(X1, X2, Z, cmap='viridis')
  ax1.set_xlabel('X1')
  ax1.set_ylabel('X2')
  ax1.set_zlabel('Objective Value')
  ax1.set_title('3D Plot of the Objective Function')

  # Scatter Plot for final values
  ax2 = fig.add_subplot(122)
  x_axis = np.arange(1, rounds + 1)
  ax2.scatter(x_axis, final_values, color='blue')
  ax2.set_xlabel('Round')
  ax2.set_ylabel('Objective Value')
  ax2.set_title('Final Values of Each Execution')

  # Frequency Table by Interval
  final_values = np.round(final_values, 3)
  min_val = int(np.floor(min(final_values)))
  max_val = int(np.ceil(max(final_values)))
  bins = np.arange(min_val, max_val + 2, 1)
  counts, bin_edges = np.histogram(final_values, bins=bins)
  df = pd.DataFrame({
      'Intervalo': [f'{edge}-{edge+1}' for edge in bin_edges[:-1]],
      'Ocorrências': counts
  })
  df = df[df['Ocorrências'] > 0]
  
  print("\nFrequência das Soluções Encontradas por Intervalo:")
  print(df)

  plt.tight_layout()
  plt.show()

