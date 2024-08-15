# Projeto: Algoritmo Genético para o Problema do Caixeiro-Viajante (TSP)

Este projeto implementa um Algoritmo Genético (AG) para resolver o Problema do Caixeiro Viajante (TSP), utilizando o conjunto de dados "brazil58" da biblioteca TSPLIB. O objetivo do projeto é encontrar uma rota que minimize a distância total percorrida ao visitar um conjunto de 58 cidades brasileiras, retornando ao ponto de partida.

## Descrição do Problema

O Problema do Caixeiro Viajante (TSP) é um problema clássico de otimização combinatória em que um vendedor deve visitar uma série de cidades, passando por cada uma exatamente uma vez e retornando à cidade de origem. O desafio é determinar a rota mais curta possível.

Neste projeto, utilizamos o conjunto de dados "brazil58" da TSPLIB, que contém as distâncias entre 58 cidades no Brasil.

## Conjunto de Dados

O conjunto de dados "brazil58" está disponível na biblioteca TSPLIB e pode ser acessado nos seguintes formatos:

- Formato `.tsp`: [brazil58.tsp](http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/brazil58.tsp)
- Formato `.xml`: [XML-TSPLIB Instances](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/XML-TSPLIB/instances/)

O formato `.tsp` apresenta os custos das distâncias entre as cidades no formato de uma matriz de incidência superior (sem as diagonais) de um grafo simétrico.

Para mais informações sobre o formato dos arquivos e o conjunto de dados, consulte o documento oficial da TSPLIB: [TSPLIB95 Documentation](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp95.pdf).

## Estrutura do Projeto

- **src/**: Contém o código-fonte do Algoritmo Genético para resolver o TSP.
- **data/**: Diretório para armazenar o arquivo "brazil58.tsp".
- **results/**: Armazena os resultados das execuções, incluindo as melhores rotas encontradas.
- **README.md**: Este arquivo, fornecendo uma visão geral do projeto.

