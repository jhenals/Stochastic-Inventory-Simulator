import numpy as np

def newsvendor_simulation(mean, stddev, production_quantity, selling_price, cost_per_unit, salvage_value,num_trials=1000):
    total_profit = 0

    for _ in range(num_trials): #each loop represents one simulated "day"
        demand=np.random.normal(mean,stddev)
        demand= int(max(0,round(demand)))
        sales= min(demand,production_quantity)
        unsold= max(0,production_quantity-demand)

        profit=(sales*selling_price)-(production_quantity*cost_per_unit) + (unsold*salvage_value)

        total_profit += profit

    average_profit= total_profit/num_trials
    return average_profit
