import os
from individuo import Individuo
from dataset_manager import load_data

class AlgoritmoGenetico:

    def __init__(self, cities):
        self.cities = cities

    def generate_population(self, population_size):
        population = []

        for _ in range(population_size):
            individual = Individuo()  # Cria um novo indivíduo
            individual.calculate_fitness(self.cities)  # Calcula o fitness do indivíduo
            population.append(individual)
        return population
    
    def print_population(population):
        for individual in population:
            print(individual)

cities = load_data(os.path.join('data', 'brazil58.xml'))
ag = AlgoritmoGenetico(cities)
ag.generate_population(10)