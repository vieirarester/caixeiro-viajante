import os
import sys
import tkinter as tk
from tkinter import messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from GeneticAlgorithm import GeneticAlgorithm
from DatasetManager import load_data

class GeneticAlgorithmInterface:
    def __init__(self, master):
        self.master = master
        master.title("AG - Caxeiro Viajante")
        master.geometry("350x250")  # Aumenta o tamanho da janela
        master.configure(bg='lightblue')  # Define a cor de fundo da janela

        # Frame principal para os widgets
        self.frame = tk.Frame(master, bg='lightblue', padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        # criando os labels e campos de entrada
        self.label_executions = tk.Label(self.frame, text="Número de Execuções", bg='lightblue')
        self.label_executions.grid(row=0, column=0, sticky='e', pady=5)

        self.entry_executions = tk.Entry(self.frame)
        self.entry_executions.grid(row=0, column=1, pady=5)

        self.label_generations = tk.Label(self.frame, text="Número de Gerações", bg='lightblue')
        self.label_generations.grid(row=1, column=0, sticky='e', pady=5)

        self.entry_generations = tk.Entry(self.frame)
        self.entry_generations.grid(row=1, column=1, pady=5)

        self.label_populations = tk.Label(self.frame, text="Tamanho da População", bg='lightblue')
        self.label_populations.grid(row=2, column=0, sticky='e', pady=5)

        self.entry_populations = tk.Entry(self.frame)
        self.entry_populations.grid(row=2, column=1, pady=5)

    def get_parameters(self):
        number_executions = int(self.entry_executions.get())
        number_generations = int(self.entry_generations.get())
        size_population = int(self.entry_populations.get())
        return number_executions, number_generations, size_population

