import tkinter as tk
from tkinter import ttk

from stochasticInventorySimulator.find_optimal_opt import find_optimal_opt
from stochasticInventorySimulator.newsvendor_simulation import newsvendor_simulation

optimize=False

def reset():
    selling_price_entry.delete(0,tk.END)
    cost_per_unit_entry.delete(0,tk.END)
    salvage_value_entry.delete(0,tk.END)
    quantity_entry.insert(0, "")
    start_quantity_entry.delete(0,tk.END)
    start_quantity_entry.insert(0, "800")
    end_quantity_entry.delete(0,tk.END)
    end_quantity_entry.insert(0, "1200")
    trial_entry.delete(0,tk.END)
    trial_entry.insert(0, "1000")

    result_label.config(text=f"")

    if optimize:
        start_quantity_entry.insert(0, "")
        end_quantity_entry.insert(0, "")
        result_label.config(text=f"")

def run_simulation():
    global optimize

    mean= int(mean_entry.get())
    stddev= int(stddev_entry.get())
    quantity = int (quantity_entry.get()) if quantity_entry.get() else None
    selling_price= int(selling_price_entry.get())
    cost_per_unit=int(cost_per_unit_entry.get())
    salvage_value=int(salvage_value_entry.get())

    if not optimize and quantity:
        profit= newsvendor_simulation(mean, stddev, quantity, selling_price, cost_per_unit, salvage_value)
        result_label.config(text=f"Average Profit: ${profit:.2f}")
        quantity_entry.insert(0,"")


    elif not optimize and not quantity:
        result_label.config(text=f"Please insert production quantity.")
    else:
        start_quantity = int(start_quantity_entry.get())
        end_quantity = int(end_quantity_entry.get())
        optimal_quantity, max_profit = find_optimal_opt(mean, stddev, selling_price,cost_per_unit, salvage_value,start_quantity, end_quantity)
        result_label.config(text=f"Optimal Quantity: {optimal_quantity}, Max Profit: ${max_profit:.2f}")



def show_optimize_widgets():
    global optimize
    optimize = True

    # Hide 1st grid
    mean_label.grid_forget()
    mean_entry.grid_forget()
    stddev_label.grid_forget()
    stddev_entry.grid_forget()
    quantity_label.grid_forget()
    quantity_entry.grid_forget()
    trial_label.grid_forget()
    trial_entry.grid_forget()
    optimize_button.grid_forget()

    # Show 2nd grid
    start_quantity_label.grid(row=1, column=0)
    start_quantity_entry.grid(row=1, column=1)
    start_quantity_entry.delete(0,tk.END)
    start_quantity_entry.insert(0, "800")  # Default value

    end_quantity_label.grid(row=2, column=0)
    end_quantity_entry.grid(row=2, column=1)
    end_quantity_entry.delete(0,tk.END)
    end_quantity_entry.insert(0, "1200")  # Default value

    selling_price_label.grid(row=4, column=0)
    selling_price_entry.grid(row=4, column=1)
    cost_per_unit_label.grid(row=5, column=0)
    cost_per_unit_entry.grid(row=5, column=1)
    salvage_value_label.grid(row=6, column=0)
    salvage_value_entry.grid(row=6, column=1)

    simulate_button.grid(row=9, column=0, columnspan=2)

    result_label.config(text=f"")
    reset()

def show_simulation_widgets():
    global optimize
    optimize = False
    start_quantity_label.grid_forget()
    start_quantity_entry.grid_forget()
    end_quantity_label.grid_forget()
    end_quantity_entry.grid_forget()
    simulate_button.grid_forget()

    mean_label.grid(row=1, column=0)
    mean_entry.grid(row=1, column=1)
    stddev_label.grid(row=2, column=0)
    stddev_entry.grid(row=2, column=1)
    quantity_label.grid(row=3, column=0)
    quantity_entry.grid(row=3, column=1)
    selling_price_label.grid(row=4, column=0)
    selling_price_entry.grid(row=4, column=1)
    cost_per_unit_label.grid(row=5, column=0)
    cost_per_unit_entry.grid(row=5, column=1)
    salvage_value_label.grid(row=6, column=0)
    salvage_value_entry.grid(row=6, column=1)
    trial_label.grid(row=7, column=0)
    trial_entry.grid(row=7, column=1)

    optimize_button.grid(row=9, column=0, columnspan=2)

    result_label.config(text=f"")
    reset()


#GUI
window=tk.Tk()
window.geometry("600x500")
window.title("Stochastic Inventory Simulation")

reset_button = ttk.Button(window, text="Reset", command=reset)
reset_button.grid(row=0, column=0, columnspan=2)


mean_label= ttk.Label(window, text="Mean Demand:")
mean_entry = ttk.Entry(window)

stddev_label= ttk.Label(window, text="Standard Deviation:")
stddev_entry = ttk.Entry(window)

quantity_label= ttk.Label(window, text="Production Quantity:")
quantity_entry = ttk.Entry(window)

selling_price_label= ttk.Label(window, text="Your Selling Price:")
selling_price_entry = ttk.Entry(window)

cost_per_unit_label= ttk.Label(window, text="Cost per Unit:")
cost_per_unit_entry = ttk.Entry(window)

salvage_value_label= ttk.Label(window, text="Salvage Value:")
salvage_value_entry = ttk.Entry(window)

trial_label= ttk.Label(window, text="Desired number of trials:")
trial_entry = ttk.Entry(window)

start_quantity_label = ttk.Label(window, text="Start Quantity:")
start_quantity_entry = ttk.Entry(window)

end_quantity_label = ttk.Label(window, text="End Quantity:")
end_quantity_entry = ttk.Entry(window)


result_label = ttk.Label(window, text="")
result_label.grid(row=10, column=0)



mean_label.grid(row=1, column=0)
mean_entry.grid(row=1, column=1)
mean_entry.insert(0,"1000") #Default value4

stddev_label.grid(row=2, column=0)
stddev_entry.grid(row=2, column=1)
stddev_entry.insert(0,"200") #Default value4

quantity_label.grid(row=3, column=0)
quantity_entry.grid(row=3, column=1)

selling_price_label.grid(row=4, column=0)
selling_price_entry.grid(row=4, column=1)

cost_per_unit_label.grid(row=5, column=0)
cost_per_unit_entry.grid(row=5, column=1)

salvage_value_label.grid(row=6, column=0)
salvage_value_entry.grid(row=6, column=1)

trial_label.grid(row=7, column=0)
trial_entry.grid(row=7, column=1)
trial_entry.insert(0,"1000")

run_button = ttk.Button(window, text="Run Simulation", command=run_simulation)
run_button.grid(row=8, column=0, columnspan=2)

optimize_button = ttk.Button(window, text="Optimize", command=show_optimize_widgets)
optimize_button.grid(row=9, column=0, columnspan=2)

simulate_button = ttk.Button(window, text="Simulate", command=show_simulation_widgets)
simulate_button.grid_forget()

#Second Grid
start_quantity_label.grid_forget()
start_quantity_entry .grid_forget()

end_quantity_label.grid_forget()
end_quantity_entry.grid_forget()

#Result


window.mainloop()

