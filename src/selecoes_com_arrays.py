import numpy as np
km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])
dados = np.array([km, anos])

# As duas linhas abaixo acessam exatamente o mesmo item do array: linha 1, coluna 2
print(dados[1][2])
print(dados[1,2])

# Slicing de arrays
contador = np.arange(0,10) # Gera o array [0 1 2 3 4 5 6 7 8 9]
# Vai extrair do elemento 1 até o elemento 7 (o 8 não entra), porém indo de 2 em 2.
print(contador[1:8:2]) # [1 3 5 7]
# Pegando todos os números pares
print(contador[::2]) # Imprime [0 2 4 6 8]
# Pegando todos os números ímpares
print(contador[1::2]) # Imprime [1 3 5 7 9]

# Calculando a kilometragem média do segundo, terceiro e quarto veículos no array de dados.
# dados[:, 1:4] retorna um array de duas linhas contendo somente os elementos das colunas 1, 2 e 3. A
# primeira linha desse array retornado contém as kilometragens; a segunda linha contém o ano de fabricação
# dos veículos. Por isso o cálculo abaixo é feito dividindo-se as colunas da linha 0 pelas colunas da linha 1.
print(dados[:, 1:4][0] / (2022 - dados[:, 1:4][1]))

# É possível gerar um array de booleans com base em alguma condição aplicada sobre o array. O exemplo abaixo
# irá gerar um array da mesma dimensão do array 'contador' sendo que cada elemento conterá True ou False
# dependendo do valor ser maior que 5 ou não.
print(contador)
contador_bool = contador > 5
print(contador_bool) # Resultado: [False False False False False False  True  True  True  True]

# Para obter do array dados somente as informações dos veículos fabricados após 2000:
print(dados[:, dados[1] > 2000])
'''
O resultado do comando acima será:
    [[44410.     0. 25757.]
     [ 2003.  2019.  2006.]]

Como se vê, o Numpy preservou a estrutura original do array (2 linhas), retornando apenas os dados das colunas
que safistazem à condição.
'''
# Calculando a kilometragem média dos veículos fabricados após o ano 2000.
print(dados[:, dados[1] > 2000][0] / (2022 - dados[:, dados[1] > 2000][1]))


