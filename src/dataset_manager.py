import xml.etree.ElementTree as ET
import os

# Caminho para o arquivo XML
dataset_xml = os.path.join('data', 'brazil58.xml')

def load_data(dataset_xml):

    try:
        # Carregar o arquivo XML
        tree = ET.parse(dataset_xml)
        root = tree.getroot()

        print(root.tag)

    except FileNotFoundError or ET.ParseError as e:
        print(f'Erro na leitura da base dados: Caminho = {dataset_xml} | {e}')
