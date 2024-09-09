from hillclimbing import hill_climbing_template
import numpy as np

def objective_function(x1, x2):
  return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + x2**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))) + 20 + np.exp(1)

lower_bounds = [-8, -8]
upper_bounds = [8, 8]
epsilon = 0.01

hill_climbing_template(
    objective_function=objective_function,
    lower_bounds=lower_bounds,
    upper_bounds=upper_bounds,
    epsilon=epsilon,
    maximize=False)
bp = 1