import os
from genetic_algorithm import GeneticAlgorithm
from dataset_manager import load_data
import matplotlib.pyplot as plt

def run_genetic_algorithm(number_executions, number_generations, size_population, cities):
    evolution_average = [0] * (number_generations + 1)

    for execution in range(number_executions):
        print(f"\n------------------------ EXECUÇÃO [{execution}/{number_executions-1}] -----------------------")
        ga = GeneticAlgorithm(cities, number_generations, size_population)
        all_generations_fitness = ga.run()

        # verifica se a lista tem o tamanho esperado
        if len(all_generations_fitness) != len(evolution_average):
            raise ValueError("O tamanho de all_generations_fitness não corresponde ao tamanho esperado.")

        for i in range(len(all_generations_fitness)):
            evolution_average[i] += all_generations_fitness[i]

    evolution_average = [fitness / number_executions for fitness in evolution_average]

    print(evolution_average)
    return evolution_average

if __name__ == "__main__":
    number_executions = 10
    number_generations = 100
    size_population = 50

    cities = load_data(os.path.join('data', 'brazil58.xml'))

    evolution_average = run_genetic_algorithm(number_executions, number_generations, size_population, cities)

    plt.plot(range(number_generations + 1), evolution_average)
    plt.xlabel('Gerações')
    plt.ylabel('Fitness (Distância Total)')
    plt.title('Evolução do Fitness ao Longo das Gerações')
    plt.show()
