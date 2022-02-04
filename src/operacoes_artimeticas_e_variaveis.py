# O operador matemático // realiza uma divisão mas retorna apenas a parte inteira do resultado
print(10 // 3) # Retorna 3 em vez de 3.3333

# Exponenciação
print(2 ** 3) # Retorna 8

# Módulo
print(10 % 3) # Retorna 1 pois 10 / 3 é 3 com resto 1.

# No modo interativo, o underline funciona como uma memória e contém o valor da última varíavel NUMÉRICA
# manipulada

# Em operações de divisão o Python retorna um valor de ponto flutuante.

# Python permite a declaração múltipla de variáveis em uma única linha
ano_atual, ano_fabricacao, km_total = 2019, 2003, 44410.0

# Python não tem conversão implícita de números par Strings em operações do tipo
a = 'Python é '
b = 'legal'
c = 10
# print(a + c) # Dá erro
print(a + str(c))

# Ao converter um número de ponto flutuante para um inteiro Python NÃO FAZ ARREDONDAMENTO. Ela vai tão somente
# pegar a parte inteira do número. Por exemplo:
n = 3.99
m = int(n)
print(m) # Resulta em 3 e não em 4 como seria o caso se houvesse arredondamento.

A = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro']
B = ['Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva']

# O operador +, em se tratando de listas irá concatenar as listas envolvidas na operação. Em outras palavras:
# criará uma nova lista contendo os elementos das listas somadas.
print(f'A lista A tem {len(A)} elementos')
print(f'A lista B tem {len(B)} elementos')
C = A + B
print(C)
print(f'A lista C tem {len(C)} elementos')

Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, ['Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, ['Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]
Carros = [Carro_1, Carro_2]
print('Travas elétricas' in Carros[0][5]) # Retorna True
print(Carros[0][-2][-1]) # Imprime Piloto automático

# Exemplo de list comprehensions em Python
[i ** 2 for i in range(10)] # O resultado será a lista [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Para criar uma lista a partir de um set (para remover duplicatas) gerado com base em uma lista
# contendo listas:
dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
resultado = list(set([item for lista in dados for item in lista]))
print(resultado)

# Lembre-se que o operador de soma (+), quando aplicado em duas listas, retorna a concatenação
# destas listas. Portanto, o código
result_2 = []
for lista in dados:
    result_2 += lista
print(result_2)
'''
resulta em 

[
    'Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 
    'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva', 'Central multimídia', 
    'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 
    'Câmera de estacionamento', 'Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 
    'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos'
]
'''

dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
# Teste == omitido já que lista[2] já retorna um boolean
veiculos_zerokm = [lista for lista in dados if lista[2]]
print(f'Veículos 0 KM: {veiculos_zerokm}')