import numpy as np
from time import time

# Criando um array numpy
anumpy = np.arange(10)
print(anumpy)

# Outra forma de se utilizar o arange é importar somente esse módulo
# from numpy import arange

# Nesse caso, para usar arange não há a necessidade de prefixar com numpy. ou np.
# anumpy2 = arange(10)
# print(anumpy2)

# Criando um array Numpy a partir de uma lista
km = np.array([1000, 2338, 3675, 44200])
print(km)
print(f'A variável km é do tipo {type(km)} e também do tipo {km.dtype}')

# Criando um Numpy array a partir de um arquivo
# Define que os dados devem ser carregados como números inteiros (o default é float).
km = np.loadtxt(fname="./data/carros-km.txt", dtype=int)
print(km)

dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]

# A linha abaixo criará um array bidimensional de 3 linhas com 8 colunas como pode ser visto na saída do comando
# acessorios.shape
acessorios = np.array(dados)
print(f'A dimensão do array acessorios é {acessorios.shape}')

# Comparando a performance de listas nativas do Python com arrays do Numpy
np_array = np.arange(1000000)
py_list = list(range(1000000))

# Comparando a performance de listas Python com arrays Numpy. O comando %time mede o tempo gasto na execução
# do comando que aparece à sua frente. Observação:  infelizmente isso não funciona aqui no PyCharm.
# %time for _ in range(100): np_array *= 2
# %time for _ in range(100): py_list = [x * 2 for x in py_list]