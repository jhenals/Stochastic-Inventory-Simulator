import tkinter as tk
from tkinter import ttk

from find_optimal_opt import find_optimal_opt
from newsvendor_simulation import newsvendor_simulation


def run_simulation():
    mean= int(mean_entry.get())
    stddev= int(stddev_entry.get())
    quantity = int (quantity_entry.get()) if quantity_entry.get() else None

    if quantity:
        profit= newsvendor_simulation(mean, stddev, quantity)
        result_label.config(text=f"Average Profit: ${profit:.2f}")

    else:
        #Optimization
        start_quantity=800
        end_quantity=1200

        step_size=25
        #optimal_quantity, max_profit = find_optimal(mean, stddev, start_quantity, end_quantity, step_size)
        optimal_quantity, max_profit = find_optimal_opt(mean, stddev, start_quantity, end_quantity)
        result_label.config(text=f"Optimal Quantity: {optimal_quantity}, Max Profit: ${max_profit:.2f}")

root=tk.Tk()
root.title("Stochastic Inventory Simulation")

mean_label= ttk.Label(root, text="Mean Demand:")
mean_label.grid(row=0, column=0)
mean_entry = ttk.Entry(root)
mean_entry.grid(row=0, column=1)
mean_entry.insert(0,"1000") #Default value4

stddev_label= ttk.Label(root, text="Standard Deviation:")
stddev_label.grid(row=1, column=0)
stddev_entry = ttk.Entry(root)
stddev_entry.grid(row=1, column=1)
stddev_entry.insert(0,"200") #Default value4

quantity_label= ttk.Label(root, text="Production Quantity:")
quantity_label.grid(row=2, column=0)
quantity_entry = ttk.Entry(root)
quantity_entry.grid(row=2, column=1)

trial_label= ttk.Label(root, text="Desired number of trials:")
trial_label.grid(row=3, column=0)
trial_entry = ttk.Entry(root)
trial_entry.grid(row=3, column=1)
trial_entry.insert(0,"1000")

run_button = ttk.Button(root, text="Run Simulation", command=run_simulation)
run_button.grid(row=4, column=0, columnspan=2)

result_label = ttk.Label(root, text="")
result_label.grid(row=5, column=0)

root.mainloop()

