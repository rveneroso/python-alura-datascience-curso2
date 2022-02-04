import numpy as np

# Listas nativas do Python
py_km = [44410., 5712., 37123., 0., 25757.]
py_anos = [2003, 1991, 1990, 2019, 2006]

# Arrays Numpy
np_km = np.array([44410., 5712., 37123., 0., 25757.])
np_anos = np.array([2003, 1991, 1990, 2019, 2006])

# Com listas nativas do Python não é possível realizar a operação abaixo:
# 2019 - py_anos -> resulta em erro

# Já com arrays Numpy a operação é válida:
idades_veiculos = 2019 - np_anos
print(idades_veiculos)

# Calculando a kilometragem média dos veículos
km_media = np_anos / idades_veiculos # Exibe mensagem de alerta sobre divisão por zero.
print(km_media)

# Criando um array bidimensional a partir de duas listas. O array abaixo terá uma dimensão de 2 x 5
# (duas linhas e cinco colunas).
array_bidimensional = np.array([py_km, py_anos])
print(array_bidimensional.shape)
print(f'A primeira linha do array contém {array_bidimensional[0]}') # Imprime a primeira linha
print(f'A segunda linha do array contém {array_bidimensional[1]}') # Imprime a segunda linha

# Calculando a kilometragem média dos veículos com base nas duas dimensões do array acima. Lembrando que
# array_bidimensional[0] contém a kilometragem total dos veículos e array_bidimensional[1] contém o ano de
# fabricação dos veículos.
km_media = array_bidimensional[0] / (2022 - array_bidimensional[1])
print(km_media)
