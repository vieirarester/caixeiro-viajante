import os
import tkinter as tk
import matplotlib.pyplot as plt

from gui.GeneticAlgorithmInterface import GeneticAlgorithmInterface
from src.GeneticAlgorithm import GeneticAlgorithm
from DatasetManager import load_data

class Main:

    def __init__(self):
        # cria e configura a janela principal
        self.root = tk.Tk()
        self.interface = GeneticAlgorithmInterface(self.root)

        self.button_run = tk.Button(self.root, text="Executar", command=self.runApp, bg='lightgreen', padx=10, pady=5)
        self.button_run.pack(pady=10)

        self.root.mainloop()

    def plot_results(self, evolution_average):
        plt.plot(range(len(evolution_average)), evolution_average)
        plt.xlabel('Gerações')
        plt.ylabel('Fitness (Distância Total)')
        plt.title('Evolução do Fitness ao Longo das Gerações')
        plt.show()

    def run_genetic_algorithm(self, number_executions, number_generations, size_population, cities):
        evolution_average = [0] * (number_generations + 1)

        for execution in range(number_executions):
            print(f"\n------------------------ EXECUÇÃO [{execution}/{number_executions-1}] -----------------------")
            ga = GeneticAlgorithm(cities, number_generations, size_population)
            all_generations_fitness = ga.run()

            for i in range(len(all_generations_fitness)):
                evolution_average[i] += all_generations_fitness[i]

        evolution_average = [fitness / number_executions for fitness in evolution_average]

        print(evolution_average)
        return evolution_average

    def runApp(self):
        cities = load_data(os.path.join('data', 'brazil58.xml'))
        # obter os parâmetros da interface
        number_executions, number_generations, size_population = self.interface.get_parameters()

        evolution_average = self.run_genetic_algorithm(number_executions, number_generations, size_population, cities)
        self.plot_results(evolution_average)

if __name__ == "__main__":
    app = Main()
    app.runApp()