import numpy as np

def cost_function(cpu_allocations):
    return np.sum(cpu_allocations * 0.1)

def latency_constraint(cpu_allocations, workloads):
    return all(cpu_allocations[i] >= workloads[i] for i in range(len(workloads)))
