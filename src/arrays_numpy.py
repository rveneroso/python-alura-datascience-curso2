import numpy as np

km = np.loadtxt('../data/carros-km.txt')

anos = np.loadtxt('../data/carros-anos.txt', dtype=int) # Informa ao Numpy para carregar os dados como inteiros.

# No cálculo abaixo, se algum elemento do array anos tivesse o valor 2022, o valor do denominador seria zero.
# Nesse caso o Numpy iria emitir uma mensagem de alerta e colocaria no resultado envolvendo esses elementos
# o nan(not a number)
km_media = km / (2022 - anos)
print(km_media)
