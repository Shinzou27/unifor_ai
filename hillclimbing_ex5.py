from hillclimbing import hill_climbing
import numpy as np

lower_bounds = [-10, -10]
upper_bounds = [10, 10]

def objective_function(x1, x2):
  return (x1 * np.cos(x1) / 20) + 2 * np.exp(-(x1)**2 - (x2 - 1)**2) + 0.01 * x1 * x2

hill_climbing(
  objective_function=objective_function,
  lower_bounds=lower_bounds,
  upper_bounds=upper_bounds,
  epsilon=0.01,
  maximize=True,
)
bp = 1