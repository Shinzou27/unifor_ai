import numpy as np
from hillclimbing import hill_climbing_template as hc
from localrandomsearch import local_random_search_template as lrs
from globalrandomsearch import global_random_search_template as grs
algorithms = {
  "hc": hc,
  "lrs": lrs,
  "grs": grs
}

def objective_function(x1, x2):
  return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + x2**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))) + 20 + np.exp(1)

lower_bounds = [-8, -8]
upper_bounds = [8, 8]
method = "hc"
epsilon = 0.5 # Somente para o HC/LRS
max_nbh = 20 # Somente para o HC
earlystopping = 1000 # Somente para o LRS

algorithms[method](
  objective_function=objective_function,
  lower_bounds=lower_bounds,
  upper_bounds=upper_bounds,
  epsilon=epsilon,
  earlystopping=earlystopping,
  maximize=False
)
