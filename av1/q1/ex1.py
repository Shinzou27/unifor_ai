from hillclimbing import hill_climbing_template as hc
from localrandomsearch import local_random_search_template as lrs
from globalrandomsearch import global_random_search_template as grs
algorithms = {
  "hc": hc,
  "lrs": lrs,
  "grs": grs
}

def objective_function(x1, x2):
  return x1**2 + x2**2 

lower_bounds = [-100, -100]
upper_bounds = [100, 100]
method = "grs"
epsilon = 0.1 # Somente para o HC/LRS
max_nbh = 20 # Somente para o HC
earlystopping = 50 # Somente para o LRS

algorithms[method](
  objective_function=objective_function,
  lower_bounds=lower_bounds,
  upper_bounds=upper_bounds,
  epsilon=epsilon,
  max_nbh=max_nbh,
  earlystopping=earlystopping,
  maximize=False
)