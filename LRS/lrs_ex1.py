from localrandomsearch import local_random_search_template as lrs

def objective_function(x1, x2):
  return x1**2 + x2**2 

lower_bounds = [-100, -100]
upper_bounds = [100, 100]
epsilon = 0.1
earlystopping = 50

lrs(
  objective_function=objective_function,
  lower_bounds=lower_bounds,
  upper_bounds=upper_bounds,
  epsilon=epsilon,
  earlystopping=earlystopping,
  maximize=False
)