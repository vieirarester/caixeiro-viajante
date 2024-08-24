import random
import os
from dataset_manager import load_data

class Individuo:
    
    def __init__(self, genes=None):
        # Se os genes não forem fornecidos, inicialize aleatoriamente
        if genes is None:
            self.genes = random.sample(range(58), 58)  # permutação das cidades
        else:
            self.genes = genes
        self.fitness = 0.0
        assert all(0 <= gene < 58 for gene in self.genes), "Valores fora do intervalo de cidades"

    def calculate_fitness(self, cities):
        total_distance = 0
        for i in range(len(self.genes) - 1):
            origin = self.genes[i]
            destination = self.genes[i + 1]

            # Verifica a distância em ambas as direções
            try:
                distance = cities[origin][destination]
            except KeyError:
                try:
                    distance = cities[destination][origin]
                except KeyError:
                    raise KeyError(f"Distância entre {origin} e {destination} não encontrada.")

            total_distance += distance

        # Adiciona a distância de retorno à cidade inicial
        try:
            total_distance += cities[self.genes[-1]][self.genes[0]]
        except KeyError:
            try:
                total_distance += cities[self.genes[0]][self.genes[-1]]
            except KeyError:
                raise KeyError(f"Distância entre {self.genes[-1]} e {self.genes[0]} não encontrada.")

        print(f"Total Distance: {total_distance}")
        self.fitness = total_distance

    def __str__(self):
        return f'Individuo(genes = {self.genes}, fitness = {self.fitness:.2f})'

# Carregar os dados e criar um indivíduo
cities = load_data(os.path.join('data', 'brazil58.xml'))
individuo = Individuo()
individuo.calculate_fitness(cities)
print(individuo)
