from scipy.optimize import minimize_scalar

from newsvendor_simulation import newsvendor_simulation


def find_optimal_opt(mean, stddev, start_quantity, end_quantity, num_trials=10000):

    def profit_to_minimize(quantity):
        profit=newsvendor_simulation(mean, stddev, quantity, num_trials)
        return -profit

    result=minimize_scalar(profit_to_minimize, bounds=(start_quantity,end_quantity), method='bounded')
    optimal_quantity=int(result.x)
    max_profit = -result.fun

    return optimal_quantity, max_profit