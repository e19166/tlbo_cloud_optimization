import unittest
import numpy as np
from src.tlbo import TLBO

class TestTLBO(unittest.TestCase):
    def setUp(self):
        """
        Set up common test data and parameters for use in test cases.
        """
        self.vm_workloads = [50, 70, 30, 90]  # Example workloads in percentage utilization
        self.num_vms = len(self.vm_workloads)
        self.optimizer = TLBO(
            num_vms=self.num_vms,
            vm_workloads=self.vm_workloads,
            population_size=10,
            iterations=50
        )

    def test_initial_population(self):
        """
        Test if the initial population is correctly initialized.
        """
        population = self.optimizer.initialize_population()
        self.assertEqual(population.shape, (self.optimizer.population_size, self.num_vms))
        self.assertTrue(np.all((population >= 0) & (population <= 100)), 
                        "All values in the initial population should be within the range [0, 100].")

    def test_evaluate_population(self):
        """
        Test if the evaluation of the population produces valid fitness scores.
        """
        fitness = self.optimizer.evaluate_population()
        self.assertEqual(len(fitness), self.optimizer.population_size)
        self.assertTrue(all(isinstance(f, float) for f in fitness), 
                        "Fitness scores should be of type float.")

    def test_teacher_phase(self):
        """
        Test if the teacher phase updates the population correctly.
        """
        old_population = self.optimizer.population.copy()
        self.optimizer.teacher_phase()
        new_population = self.optimizer.population

        self.assertEqual(new_population.shape, old_population.shape)
        self.assertFalse(np.array_equal(old_population, new_population), 
                         "Population should change after the teacher phase.")

    def test_learner_phase(self):
        """
        Test if the learner phase updates the population correctly.
        """
        old_population = self.optimizer.population.copy()
        self.optimizer.learner_phase()
        new_population = self.optimizer.population

        self.assertEqual(new_population.shape, old_population.shape)
        self.assertFalse(np.array_equal(old_population, new_population), 
                         "Population should change after the learner phase.")

    def test_optimization(self):
        """
        Test the overall optimization process.
        """
        best_solution, best_cost = self.optimizer.optimize()
        self.assertEqual(len(best_solution), self.num_vms)
        self.assertTrue(best_cost > 0, "Best cost should be a positive value.")
        self.assertTrue(np.all((best_solution >= 0) & (best_solution <= 100)), 
                        "Final solution values should be within the range [0, 100].")

if __name__ == "__main__":
    unittest.main()
