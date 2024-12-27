import numpy as np

def mock_vm_workloads(num_vms, min_load=10, max_load=100):
    """
    Generate mock workloads for virtual machines.

    Args:
        num_vms (int): Number of virtual machines.
        min_load (int): Minimum workload percentage.
        max_load (int): Maximum workload percentage.

    Returns:
        list: List of workloads for each virtual machine.
    """
    return np.random.randint(min_load, max_load, size=num_vms).tolist()

def validate_latency_constraints(cpu_allocations, workloads):
    """
    Validate that allocated CPU meets or exceeds workload demands.

    Args:
        cpu_allocations (list): CPU allocations for each VM.
        workloads (list): Workloads for each VM.

    Returns:
        bool: True if all allocations meet or exceed workloads, False otherwise.
    """
    return all(cpu_allocations[i] >= workloads[i] for i in range(len(workloads)))

def calculate_cost(cpu_allocations, cost_per_unit=0.1):
    """
    Calculate the total cost based on CPU allocations.

    Args:
        cpu_allocations (list): CPU allocations for each VM.
        cost_per_unit (float): Cost per unit of CPU allocated.

    Returns:
        float: Total cost.
    """
    return np.sum(np.array(cpu_allocations) * cost_per_unit)

def generate_mock_population(population_size, num_vms, min_allocation=0, max_allocation=100):
    """
    Generate a mock population of CPU allocations for testing.

    Args:
        population_size (int): Number of individuals in the population.
        num_vms (int): Number of virtual machines.
        min_allocation (int): Minimum CPU allocation.
        max_allocation (int): Maximum CPU allocation.

    Returns:
        np.ndarray: Mock population of CPU allocations.
    """
    return np.random.uniform(min_allocation, max_allocation, (population_size, num_vms))
