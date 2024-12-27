import unittest
from tests.test_utils import (
    mock_vm_workloads,
    validate_latency_constraints,
    calculate_cost,
    generate_mock_population
)

class TestValidationUtils(unittest.TestCase):
    def test_mock_vm_workloads(self):
        num_vms = 5
        workloads = mock_vm_workloads(num_vms, min_load=20, max_load=80)
        self.assertEqual(len(workloads), num_vms)
        self.assertTrue(all(20 <= w <= 80 for w in workloads), 
                        "Workloads should be within the specified range.")

    def test_validate_latency_constraints_valid(self):
        cpu_allocations = [60, 80, 40, 100]
        workloads = [50, 70, 30, 90]
        self.assertTrue(validate_latency_constraints(cpu_allocations, workloads), 
                        "CPU allocations should satisfy the workloads.")

    def test_validate_latency_constraints_invalid(self):
        cpu_allocations = [50, 60, 20, 80]
        workloads = [60, 70, 30, 90]
        self.assertFalse(validate_latency_constraints(cpu_allocations, workloads), 
                         "Some CPU allocations do not satisfy the workloads.")

    def test_calculate_cost(self):
        cpu_allocations = [50, 70, 30, 90]
        cost_per_unit = 0.2
        expected_cost = sum([x * cost_per_unit for x in cpu_allocations])
        self.assertAlmostEqual(calculate_cost(cpu_allocations, cost_per_unit), expected_cost, 
                               msg="Cost calculation is incorrect.")

    def test_generate_mock_population(self):
        population_size = 10
        num_vms = 4
        population = generate_mock_population(population_size, num_vms, min_allocation=10, max_allocation=50)
        self.assertEqual(population.shape, (population_size, num_vms))
        self.assertTrue((population >= 10).all() and (population <= 50).all(),
                        "Population values should be within the specified allocation range.")

if __name__ == "__main__":
    unittest.main()
