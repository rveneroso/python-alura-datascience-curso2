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