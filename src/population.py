import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import random
from Individual import Individual
from DatasetManager import load_data

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
        current = 0
        
        # encontra o indivíduo selecionado
        for individual in self.individuals:
            current += individual.fitness
            if current > pick:
                return individual
            
    def elitism_selection(self, individuals_selected):

        # ordena a população em ordem crescente de fitness
        sorted_individuals = sorted(self.individuals, key=lambda indiv: indiv.fitness)
        best_individuals = sorted_individuals[:individuals_selected]

        return best_individuals

