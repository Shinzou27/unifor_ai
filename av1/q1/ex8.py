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
  return (
    -(x2+47)*np.sin(np.sqrt(np.abs(x1/2 + (x2+47))))-x1*np.sin(np.sqrt(np.abs(x1 - x2 + 47)))
  )

lower_bounds = [-200, -200]
upper_bounds = [20, 20]
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
  maximize=False,
)