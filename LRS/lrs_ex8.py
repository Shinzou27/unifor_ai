from localrandomsearch import local_random_search_template as lrs
import numpy as np

def objective_function(x1, x2):
  return (
    -(x2+47)*np.sin(np.sqrt(np.abs(x1/2 + (x2+47))))-x1*np.sin(np.sqrt(np.abs(x1 - x2 + 47)))
  )

lower_bounds = [-200, -200]
upper_bounds = [20, 20]
epsilon = 0.5
earlystopping = 1000

lrs(
  objective_function=objective_function,
  lower_bounds=lower_bounds,
  upper_bounds=upper_bounds,
  epsilon=epsilon,
  earlystopping=earlystopping,
  maximize=False,
)