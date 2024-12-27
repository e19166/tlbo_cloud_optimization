import matplotlib.pyplot as plt

def plot_results(vm_ids, workloads, allocations):
    plt.bar(vm_ids, workloads, label="Workload", alpha=0.7, color="blue")
    plt.bar(vm_ids, allocations, label="Allocated CPU", alpha=0.7, color="orange")
    plt.xlabel("Virtual Machines")
    plt.ylabel("CPU (%)")
    plt.legend()
    plt.show()
