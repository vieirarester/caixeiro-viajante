import random
import os
from dataset_manager import load_data

class Individual:
    
    def __init__(self, genes=None):
        # Se os genes não forem fornecidos, inicialize aleatoriamente
        if genes is None:
            self.genes = random.sample(range(58), 58)  # permutação das cidades
        else:
            self.genes = genes
        self.fitness = self.calculate_fitness(load_data(os.path.join('data', 'brazil58.xml')))
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

        self.fitness = total_distance
        return self.fitness
    
    def fill_child(self, child, parent, end):
        index = end + 1 # índice (gene) de onde vai começar a ser preenchido o indivíduo

        # percorre todos os genes do pai
        for gene in parent.genes:
            if gene not in child:

                # verifica se o índice chegou no final do indivíduo
                if index >= 58:
                    # se sim, o índice vai para o início da lista
                    index = 0
                # atribui o gene do pai à posição atual no filho
                child[index] = gene
                # move para a próxima posição (gene)
                index += 1
    
    def crossover(self, other_parent):
        # escolhe 2 pontos aleatórios entre 0 e 57
        p1, p2 = sorted(random.sample(range(58), 2))
        
        child1 = [None] * 58
        child2 = [None] * 58
        
        # copia os genes definidos entre o intervalo p1 e p2 do pai1 (self) para o filho1
        child1[p1:p2+1] = self.genes[p1:p2+1]
        # copia os genes definidos entre o intervalo p1 e p2 do pai2 (self) para o filho2
        child2[p1:p2+1] = other_parent.genes[p1:p2+1]
        
        # preenche os genes restantes dos filhos
        self.fill_child(child1, other_parent, p2)
        self.fill_child(child2, self, p2)
        
        return Individual(child1), Individual(child2)
    
    def mutate(self):
        # sorteia indíces para trocar
        index1, index2 = random.sample(range(len(self.genes)), 2)
        print(f"Os índices sorteados foram = {index1} e {index2}")

        # troca os genes com índices sorteados
        self.genes[index1], self.genes[index2] = self.genes[index2], self.genes[index1]

        return self

    def __str__(self):
        return f'Individuo(genes = {self.genes}, fitness = {self.fitness:.2f})'