import numpy as np
from src.utils import cost_function, latency_constraint

class TLBO:
    def __init__(self, num_vms, vm_workloads, population_size=10, iterations=100):
        self.num_vms = num_vms
        self.vm_workloads = vm_workloads
        self.population_size = population_size
        self.iterations = iterations
        self.population = self.initialize_population()

    def initialize_population(self):
        # Initialize CPU allocations randomly
        return np.random.uniform(0, 100, (self.population_size, self.num_vms))

    def evaluate_population(self):
        # Evaluate fitness (cost + constraints)
        fitness = []
        for individual in self.population:
            if latency_constraint(individual, self.vm_workloads):
                fitness.append(cost_function(individual))
            else:
                fitness.append(float('inf'))  # Penalize infeasible solutions
        return np.array(fitness)

    def teacher_phase(self):
        fitness = self.evaluate_population()
        best_index = np.argmin(fitness)
        best_solution = self.population[best_index]

        mean_solution = np.mean(self.population, axis=0)
        teacher_factor = np.random.randint(1, 3)  # Teacher factor is either 1 or 2
        new_population = []

        for individual in self.population:
            new_individual = individual + np.random.rand() * (best_solution - teacher_factor * mean_solution)
            new_population.append(np.clip(new_individual, 0, 100))  # Clip values to valid range

        self.population = np.array(new_population)

    def learner_phase(self):
        new_population = []
        for i, individual in enumerate(self.population):
            partner_index = np.random.choice([j for j in range(self.population_size) if j != i])
            partner = self.population[partner_index]

            if cost_function(individual) < cost_function(partner):
                new_individual = individual + np.random.rand() * (individual - partner)
            else:
                new_individual = individual + np.random.rand() * (partner - individual)

            new_population.append(np.clip(new_individual, 0, 100))

        self.population = np.array(new_population)

    def optimize(self):
        for _ in range(self.iterations):
            self.teacher_phase()
            self.learner_phase()

        # Return the best solution
        fitness = self.evaluate_population()
        best_index = np.argmin(fitness)
        print(best_index)
        return self.population[best_index], fitness[best_index]