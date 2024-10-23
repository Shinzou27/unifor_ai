from hillclimbing import hill_climbing
import numpy as np

lower_bounds = [-1, -1]
upper_bounds = [3, 3]

def objective_function(x1, x2):
  return x1*np.sin(4*np.pi*x1)-x2*np.sin(4*np.pi*x2 + np.pi) + 1

hill_climbing(
  objective_function=objective_function,
  lower_bounds=lower_bounds,
  upper_bounds=upper_bounds,
  epsilon=0.1,
  maximize=True,
)
bp = 1