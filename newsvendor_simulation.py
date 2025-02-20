import numpy as np

def newsvendor_simulation(mean, stddev, production_quantity, num_trials=1000):
    total_profit = 0

    for _ in range(num_trials): #each loop represents one simulated "day"
        demand=np.random.normal(mean,stddev)
        demand= int(max(0,round(demand)))
        sales= min(demand,production_quantity)
        unsold= max(0,production_quantity-demand)

        profit=(sales*25)-(production_quantity*10) + (unsold*5)

        total_profit += profit

    average_profit= total_profit/num_trials
    return average_profit
