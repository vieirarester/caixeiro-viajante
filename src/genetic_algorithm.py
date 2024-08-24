import os
from individual import Individual
from dataset_manager import load_data

class GeneticAlgorithm:

    def __init__(self, cities):
        self.cities = cities

    
cities = load_data(os.path.join('data', 'brazil58.xml'))