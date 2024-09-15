from localrandomsearch import local_random_search_template as lrs
import numpy as np

def objective_function(x1, x2):
  return x1*np.sin(4*np.pi*x1)-x2*np.sin(4*np.pi*x2 + np.pi) + 1

lower_bounds = [-1, -1]
upper_bounds = [3, 3]
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