def validate_solution(solution, workloads):
    if all(solution[i] >= workloads[i] for i in range(len(workloads))):
        return "Feasible solution."
    return "Solution violates latency constraints."
