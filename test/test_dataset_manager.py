import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from dataset_manager import load_data

class TestDatasetManager(unittest.TestCase):

    def setUp(self):
        # executa antes de cada execução
        self.cities = load_data('../data/brazil58.xml')

    def test_complete_file_load(self):
     self.assertIsNotNone(self.cities, "O arquivo não foi carregado.")

    def test_distances_are_correct(self):
        self.assertEqual(self.cities[0][1], 2635.0, "Distância da Cidade 0 para Cidade 1 incorreta!")
        self.assertEqual(self.cities[1][2], 314.0, "Distância da Cidade 1 para Cidade 2 incorreta!")
        self.assertEqual(self.cities[2][3], 2730.0, "Distância da Cidade 2 para Cidade 3 incorreta!")
        self.assertEqual(self.cities[56][57], 962.0, "Distância da Cidade 56 para Cidade 57 incorreta!")

if __name__ == '__main__':
    unittest.main()
