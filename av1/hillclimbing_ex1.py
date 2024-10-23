from hillclimbing import hill_climbing_template

def objective_function(x1, x2):
    return x1**2 + x2**2 

lower_bounds = [-100, -100]
upper_bounds = [100, 100]
epsilon = 0.1

hill_climbing_template(
    objective_function=objective_function,
    lower_bounds=lower_bounds,
    upper_bounds=upper_bounds,
    epsilon=epsilon,
    maximize=False)
bp = 1