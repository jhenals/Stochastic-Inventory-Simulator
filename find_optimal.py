import numpy as np


from stochasticInventorySimulator.newsvendor_simulation import newsvendor_simulation


def find_optimal( mean, stddev, start_quantity, end_quantity, step_size):
    best_quantity=0
    best_profit = -np.inf

    for quantity in range(start_quantity, end_quantity, step_size):
        profit = newsvendor_simulation(mean, stddev, quantity)
        if profit > best_profit:
            best_profit = profit
            best_quantity = quantity

    #print(f"Optimal production quantity: {best_quantity}")
    return best_quantity, best_profit