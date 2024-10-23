from hillclimbing import hill_climbing
import numpy as np

lower_bounds = [-200, -200]
upper_bounds = [20, 20]

def objective_function(x1, x2):
  return (
    -(x2+47)*np.sin(np.sqrt(np.abs(x1/2 + (x2+47))))-x1*np.sin(np.sqrt(np.abs(x1 - x2 + 47)))
  )

hill_climbing(
  objective_function=objective_function,
  lower_bounds=lower_bounds,
  upper_bounds=upper_bounds,
  epsilon=0.001,
  maximize=False,
)
bp = 1