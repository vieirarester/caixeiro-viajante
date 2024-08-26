import xml.etree.ElementTree as ET
import os

# caminho para o arquivo XML
dataset_xml = os.path.join('data', 'brazil58.xml')

def load_data(dataset_xml):

    # carregar informações das cidades num dicionário
    cities = {}

    try:
        # carregar o arquivo XML
        tree = ET.parse(dataset_xml)
        root = tree.getroot()

        # encontrar todos os elementos que correspondem a expressão XPath
        for origin, city in enumerate(root.findall('.//graph/vertex')):
            for d in city.findall('edge'):
                distance = float(d.get('cost')) # conteúdo do atributo 'cost'
                id_city = int(d.text.strip()) # ID da cidade destino

                if id_city not in cities or origin not in cities[id_city]:
                    if origin not in cities:
                        cities[origin] = {}
                    cities[origin][id_city] = distance

    except (FileNotFoundError, ET.ParseError) as e:
        print(f'Erro na leitura da base dados: Caminho = {dataset_xml} | Erro: {e}')
    
    return cities
