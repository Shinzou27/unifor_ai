from localrandomsearch import local_random_search_template as lrs
import numpy as np

def objective_function(x1, x2):
  return (x1**2 - 10 * np.cos(2 * np.pi * x1) + 10) + (x2**2 - 10 * np.cos(2 * np.pi * x2) + 10)

lower_bounds = [-5.12, -5.12]
upper_bounds = [5.12, 5.12]
epsilon = 0.9
earlystopping = 1000

lrs(
  objective_function=objective_function,
  lower_bounds=lower_bounds,
  upper_bounds=upper_bounds,
  epsilon=epsilon,
  earlystopping=earlystopping,
  maximize=False,
)