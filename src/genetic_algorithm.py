import os
import random
from individual import Individual
from population import Population  # Supondo que você já tenha uma classe Population
from dataset_manager import load_data

class GeneticAlgorithm:

    def __init__(self, cities, number_generations, size_population):
        self.cities = cities
        self.number_generations = number_generations
        self.size_population = size_population

        self.population = Population(size_population, cities)

        # verifica o indivíduo na população que tem o melhor (menor) valor de fitness
        self.best_all_generations = min(self.population.individuals, key=lambda indiv: indiv.fitness)
        # armazena na lista de melhores fitness
        self.all_fitness = [self.best_all_generations.fitness]

    def run(self):
        for generation_counter in range(self.number_generations):
            new_population = []

            while len(new_population) < self.size_population:
                # seleciona os pais para cruzamento
                parent1 = self.population.roulette_wheel_selection()
                parent2 = self.population.roulette_wheel_selection()

                # cruzamento a partir dos pais selecionados
                child1, child2 = parent1.crossover(parent2)

                # aplica mutação aos filhos
                child1.mutate(0.05)
                child2.mutate(0.05)

                # adiciona filhos à nova população
                new_population.append(child1)
                new_population.append(child2)

            # atualizar a população com os novos indivíduos
            self.population.individuals = new_population

            # encontra o melhor indivíduo da geração atual
            best_current_generation = min(self.population.individuals, key=lambda indiv: indiv.fitness)

            # atualiza o melhor indivíduo de todas as gerações, caso seja válido
            if best_current_generation.fitness < self.best_all_generations.fitness:
                self.best_all_generations = best_current_generation

            self.all_fitness.append(best_current_generation.fitness)

            print(f'[Geração {generation_counter}]: O melhor = {best_current_generation.fitness} | Melhor de Todos = {self.best_all_generations.fitness}')

            return self.best_all_generations, self.all_fitness


cities = load_data(os.path.join('data', 'brazil58.xml'))
genetic_algorithm = GeneticAlgorithm(cities, number_generations=100, size_population=50)
genetic_algorithm.run()