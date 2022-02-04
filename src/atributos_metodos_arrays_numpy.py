import numpy as np
km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km, anos])

# Retorna uma tupla (linhas e colunas) de um array
print(dados.shape)

# Retorna as dimensões de um array
print(dados.ndim) # Esse array possui linhas e colunas. Portanto, possui 2 dimensões

# Retorna a quantidade de elementos de um array
print(dados.size) # Retorna 10: 2 linhas x 5 colunas

# Retorna o tipo dos elementos contidos no array
print(dados.dtype) # Retorna float64

# Retorna o transposto do array. O que for linha vira coluna e o que for coluna vira linha.
print(dados.T) # dados.transpose() gera o mesmo resultado.

# Converte um array Numpy em uma lista Python
print(dados.tolist())

# Cria um array com 1 linha e 10 colunas. Total de elementos: 10
contador = np.arange(10)
# Cria um novo contador com 2 linhas e 5 colunas a partir do array contador. O número total de elementos será o
# mesmo do array original (2 linhas x 5 colunas = 10 elementos).
novo_contador = contador.reshape((2,5))
print(novo_contador)

dados_new = dados.copy()
print(dados_new)

# Primeira tentativa de redimensionar o array adicionando uma linha.
# Passa a ter 3 linhas e continua com 5 colunas. De acordo com o instrutor, nesse ponto era para ocorrer um erro.
# O Numpy deveria indicar que não pode redimensionar um array que é uma referência ou que é referenciado por
# outro array. Como dados_new é uma cópia de dados, o erro deveria ter ocorrido. Tudo indica que essa é uma
# característica que não existe mais na versão do Python qu estou usando.
dados_new.resize((3,5))
print(dados_new)
# Se o erro tivesse ocorrido, ele poderia ser resolvido adicionando-se o parâmetro refcheck=False no resize():
dados_new.resize((3,5), refcheck=False)
print(dados_new)
# Populando a terceira linha do array com a kilometragem média dos veículos
dados_new[2] = dados_new[0] / (2022 - dados_new[1])
print(dados_new)