import random
import math
import time
def initial_state():
    """Cria um estado inicial com uma rainha em cada coluna, em uma linha aleatória."""
    return [random.randint(0, 7) for _ in range(8)]
def temperature_decrement(temperature, current, start_temp, type = 0, nt = 1000, Tnt = 0):
    if type == 0:
        return temperature * 0.99
    elif type == 1:
        return temperature/(1 + 0.99 * math.sqrt(temperature))
    elif type == 2:
        return temperature - (start_temp - Tnt) / nt
        
def objective_function(state):
    """Calcula o número de pares de rainhas que se atacam no tabuleiro."""
    attacking_pairs = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs

def neighbor(state):
    """Gera um estado vizinho, mudando a linha de uma rainha aleatória."""
    neighbor_state = state[:]
    col = random.randint(0, 7)
    new_row = state[col]
    if random.random() < 0.5:
        new_row = state[col] - 1 if state[col] > 0 else state[col] + 1
    else:
        new_row = state[col] + 1 if state[col] < 7 else state[col] - 1

    neighbor_state[col] = new_row
    return neighbor_state

def simulated_annealing(initial_state, objective_function, neighbor, start_temp = 100, max_iterations=1000, type = 0):
    """Executa o algoritmo da têmpera simulada para minimizar a função objetivo."""
    current_state = initial_state()
    current_value = objective_function(current_state)
    temperature = start_temp

    for iteration in range(max_iterations):
        if current_value == 0:
            break  # Solução ótima encontrada

        next_state = neighbor(current_state)
        next_value = objective_function(next_state)
        delta_e = next_value - current_value

        if delta_e < 0 or random.random() < math.exp(-delta_e / temperature):
            current_state = next_state
            current_value = next_value

        temperature = temperature_decrement(temperature, iteration, start_temp, type)

    return current_state, current_value

def find_all_solutions(type = 0):
    solutions = set()
    attempts = 0
    while len(solutions) < 92:
        final_state, final_value = simulated_annealing(initial_state, objective_function, neighbor, type=type)

        if final_value == 0:
            # Converte o estado em uma tupla para ser armazenado no set de soluções
            solution_tuple = tuple(final_state)
            if solution_tuple not in solutions:
                solutions.add(solution_tuple)
                print(f"Solução {len(solutions)} encontrada: {final_state}")

        attempts += 1
        if attempts % 1000 == 0:
            print(f"{attempts} tentativas realizadas, {len(solutions)} soluções encontradas.")

    return [solutions, attempts]
# Executa a busca por todas as 92 soluções
for i in range(3):
    initialTime = time.time()
    type = i
    result = find_all_solutions(type)
    finalTime = time.time()
    print(f"{len(result[0])} soluções encontradas em {result[1]} tentativas.\nTempo total de execução: {(finalTime - initialTime):.2f}s")
    print(f"\n(Utilizando o {i+1}º método de decaimento)\n")
bp = 1