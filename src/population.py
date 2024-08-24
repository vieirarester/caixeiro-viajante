import os
from individual import Individual
from dataset_manager import load_data

class Population:
    def __init__ (self, population_size, cities):
        self.individuals = []

        for _ in range(population_size):
            individual = Individual()  # cria um novo indivíduo
            individual.calculate_fitness(cities)  # calcula o fitness do indivíduo
            self.individuals.append(individual) # adiciona cada indivíduo a população
    
    def print_population(self):

        for individual in self.individuals:
            print(individual)

cities = load_data(os.path.join('data', 'brazil58.xml'))
population = Population(15, cities)
population.print_population()
