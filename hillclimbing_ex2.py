from hillclimbing import hill_climbing_template
import numpy as np

def objective_function(x1,x2):
    return np.exp(-(x1**2 + x2**2)) + 2 * np.exp(-((x1 + 1.7)**2 + (x2 + 1.7)**2))

lower_bounds = [-2,-2]
upper_bounds = [4,5]  
epsilon = 0.0001

hill_climbing_template(
    objective_function=objective_function,
    lower_bounds=lower_bounds,
    upper_bounds=upper_bounds,
    epsilon=epsilon,
    maximize=True)
bp = 1