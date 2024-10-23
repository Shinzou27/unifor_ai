from hillclimbing import hill_climbing_template
import numpy as np

lower_bounds = [-5.12, -5.12]
upper_bounds = [5.12, 5.12]

def objective_function(x1, x2):
  return (x1**2 - 10 * np.cos(2 * np.pi * x1) + 10) + (x2**2 - 10 * np.cos(2 * np.pi * x2) + 10)

hill_climbing_template(
  objective_function=objective_function,
  lower_bounds=lower_bounds,
  upper_bounds=upper_bounds,
  epsilon=0.1,
  maximize=False,
)
bp = 1