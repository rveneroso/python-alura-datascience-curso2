import numpy as np

anos = np.loadtxt(fname = "../data/carros-anos.txt", dtype = int)
km = np.loadtxt(fname = "../data/carros-km.txt")
valor = np.loadtxt(fname = "../data/carros-valor.txt")

# Para converter os 3 arrays unidimensionais acima em um array multidimensional podemos usar o método column_stack()
dataset = np.column_stack((anos, km, valor))
print(dataset.shape) # Vai exibir (258, 3) já que os arrays originais tem 1 única coluna e 258 linhas.

# Para calcular a média dos valores presentes no dataset
# No formato abaixo, o mean() vai somar todos os valores presentes no dataset e obter a média. É um número
# sem nenhum significado prático.
print(np.mean(dataset))

# Com a sintaxe abaixo, informamos ao mean() para obter a média separadamente para cada uma das colunas do
# dataset. Lembrando que as colunas representam o ano, a kilometragem e o valor, respectivamente, então o
# mean() dará a média dessas medidas.
print(np.mean(dataset, axis=0))

# Já que a média dos anos de fabricação dos veículos é uma informação irrelevante, podemos calcular as médias
# de kilometragem e de valor separadamente através de um slicing no dataset.
print(np.mean(dataset[:, 1])) # indicamos todas as linhas através do : e informamos a coluna 1 que é a kilometragem.
print(np.mean(dataset[:, 2])) # indicamos todas as linhas através do : e informamos a coluna 2 que é o valor.

# O desvio padrão pode ser calculado através do método std():
print(np.std(dataset[:, 1])) # desvio padrão da kilometragem.
print(np.std(dataset[:, 2])) # desvio padrão do valor.

# Somatório dos valores
print(dataset.sum(axis=0)) # Somatório de colunas
print(dataset.sum(axis=1)) # Somatório de linhas
print((dataset[:, 1]).sum()) # somatório da kilometragem.
print((dataset[:, 2]).sum()) # somatório dos valores.

# Outra forma de se obter o somatório
print(np.sum(dataset, axis=0)) # Somatório de colunas
print(np.sum(dataset, axis=1)) # Somatório de linhas
# Aplicando slicing no dataset
print(np.sum(dataset[:, 1])) # somatório da kilometragem.
print(np.sum(dataset[:, 2])) # somatório do valor.

