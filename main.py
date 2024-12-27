import json
from src.tlbo import TLBO
from src.validation import validate_solution
from src.visualization import plot_results

# Load workloads
with open("data/vm_workloads.json", "r") as f:
    workloads = json.load(f)["workloads"]

# Initialize TLBO
optimizer = TLBO(num_vms=len(workloads), vm_workloads=workloads)
best_solution, best_cost = optimizer.optimize()

# Validate and visualize
print(validate_solution(best_solution, workloads))
print("Optimal CPU Allocations:", best_solution)
plot_results([f"VM {i+1}" for i in range(len(workloads))], workloads, best_solution)
