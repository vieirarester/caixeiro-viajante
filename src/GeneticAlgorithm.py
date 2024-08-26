import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from Population import Population

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

            elite_individuals = self.population.elitism_selection(10)
            non_elite_individuals = [indiv for indiv in self.population.individuals if indiv not in elite_individuals]

            # adiciona os indivíduos de elite à nova população
            new_population.extend(elite_individuals)

            while len(new_population) + 2 <= self.size_population:
                # seleciona o primeiro pai para cruzamento dentre os indivíduos da elite
                parent1 = random.choice(elite_individuals)
                # seleciona o segundo pai para cruzamento dentro o restante dos indivíduos
                parent2 = random.choice(non_elite_individuals)

                # cruzamento a partir dos pais selecionados
                child1, child2 = parent1.crossover(parent2)

                # aplica mutação aos filhos
                child1.mutate(0.05)
                child2.mutate(0.05)

                # adiciona filhos à nova população
                new_population.append(child1)
                new_population.append(child2)

            while len(new_population) < self.size_population:
                # caso a população seja ímpar, pode ser necessário adicionar apenas um indivíduo
                parent1 = random.choice(elite_individuals)
                parent2 = random.choice(non_elite_individuals)
                child1, _ = parent1.crossover(parent2)
                child1.mutate(0.05)
                new_population.append(child1)

            # atualizar a população com os novos indivíduos
            self.population.individuals = new_population

            # encontra o melhor indivíduo da geração atual
            best_current_generation = min(self.population.individuals, key=lambda indiv: indiv.fitness)

            # atualiza o melhor indivíduo de todas as gerações, caso seja válido
            if best_current_generation.fitness < self.best_all_generations.fitness:
                self.best_all_generations = best_current_generation

            self.all_fitness.append(best_current_generation.fitness)

            print(f'[Geração {generation_counter}]: O melhor = {best_current_generation.fitness} | Melhor de Todos = {self.best_all_generations.fitness}')

        return self.all_fitness
