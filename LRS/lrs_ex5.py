from localrandomsearch import local_random_search_template as lrs
import numpy as np

def objective_function(x1, x2):
  return (x1 * np.cos(x1) / 20) + 2 * np.exp(-(x1)**2 - (x2 - 1)**2) + 0.01 * x1 * x2

lower_bounds = [-10, -10]
upper_bounds = [10, 10]
epsilon = 0.5
earlystopping = 1000

lrs(
  objective_function=objective_function,
  lower_bounds=lower_bounds,
  upper_bounds=upper_bounds,
  epsilon=epsilon,
  earlystopping=earlystopping,
  maximize=True,
)
