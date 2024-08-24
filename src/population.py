import os
import random
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

    def roulette_wheel_selection(self):
        # calcula o somatório dos fitness de todos os indivíduos
        total_fitness = sum(individual.fitness for individual in self.individuals)
        
        # escolhe um ponto na roleta
        pick = random.uniform(0, total_fitness)
        print(f"O ponto da roleta foi: {pick}\n")
        current = 0
        
        # encontra o indivíduo selecionado
        for individual in self.individuals:
            current += individual.fitness
            if current > pick:
                return individual

cities = load_data(os.path.join('data', 'brazil58.xml'))
population = Population(10, cities)
population.print_population()
print(population.roulette_wheel_selection())
