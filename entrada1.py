# todo: mudar a inserção na matriz_incial, ao inves de usar a ordenação como parâmetro, utilizar a referencia de classe

from itertools import groupby
from entradas1_recurso import *
import random
import numpy as np
from entradas1_semana import *
from entradas1_evento import *

evento = dict.fromkeys(idResourceGroup)

# print(referenceResourceGroup)

final = [list(referenceResourceGroup) for q, referenceResourceGroup in groupby(referenceResourceGroup)]

y = 0
lista_teste = []

"""
-----------------------------------------------------
a lista 'final' é a lista contendo as referencias dos recursos, ou seja
teachers, classes, rooms
print(f' final {final}') [['gr_Teachers', 'gr_Teachers', 'gr_Teachers', 'gr_Teachers', 'gr_Teachers', 'gr_Teachers',
 'gr_Teachers', 'gr_Teachers'], ['gr_Classes', 'gr_Classes', 'gr_Classes']]
-----------------------------------------------------
"""
# print(f' final {final}')

for i in range(len(final)):
    for j in range(len(final[i])):
        lista_teste.append(idResource[y])
        if len(lista_teste) == len(final[i]):
            evento[final[i][0]] = lista_teste
            lista_teste = []
        y += 1

"""
-----------------------------------------------------
a lista evento mostra o que cada recurso é de fato
{'gr_Teachers': ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8'], 'gr_Classes': ['S1', 'S2', 'S3']}
print(evento)
-----------------------------------------------------
"""

"""
-----------------------------------------------------
verificando a quantidade de classes pelo tamanho da da lista event na posição
da classes, utilizando o idResourceGroup ['gr_Teachers', 'gr_Classes'] na posição 1,
consegue-se verificar na lista evento a quantidade de valores daquela chave
determinando a quantidade de aulas
print(qtd_classes)
-----------------------------------------------------
"""

qtd_classes = len(evento[idResourceGroup[1]])


"""
-----------------------------------------------------
o idDuration é o dicionário dos eventos propriamente dito, nele estão todas as informações
{'T1-S1': {'duration': ['3'], 'course': ['gr_T1-S1'], 'resourceReference': ['S1', 'T1']}
a key é o proprio evento, pra facilitar
print(f'\no idDuration é {idDuration}\n')
-----------------------------------------------------
"""

turma = []

"""
-----------------------------------------------------
Pegando a duração de todos os eventos que são string e então convertendo
em int, a variavel str1 e o metodo join juntam as string entre '' e depois
são convertidos em int e inseridos na lista duracao
print(idDuration[idEvent[0]]['duration'])
print(str1)
print(duracao)
-----------------------------------------------------
"""

dict_matriz = {}
str1 = []
duracao = []

for i in range(len(idEvent)):
    str1.append(''.join(idDuration[idEvent[i]]['duration']))
    duracao.append(int(str1[i]))

"""
-----------------------------------------------------
Pegando todas as aulas (eventos) e inserindo na lista aulas
É inserido de acordo com a duração da daquela aula em específico
['T1-S1', 'T1-S1', 'T1-S1', 'T1-S2', 'T1-S2', 'T1-S2', 'T1-S3', 'T1-S3', 
print(aulas) 
-----------------------------------------------------
"""

aulas = []
for i in range(len(idEvent)):
    for j in range(duracao[i]):
        aulas.append(idEvent[i])

# print(f'aulas {aulas}')
x = 0

"""
-----------------------------------------------------
É inserido na lista_ordenada as classes ordenadas de acordo com as classes,
para que depois sejam manipulados
é utilizado a lista aulas para se chegar na chave desejada no dicionario idDuration,
utiliza-se a key "resourceReference" para se encontrar as referencias de recurso nesse evento
e então selecionar o primeiro, que é a referencia de classe
['T1-S1', 'T1-S1', 'T1-S1', 'T2-S1', 'T2-S1', 'T2-S1', 'T2-S1', 'T2-S1', 'T3-S1', 'T3-S1', 'T3-S1'
print(idDuration[aulas[0]]["resourceReference"][0])
print(f'listona {lista_ordenada}')
-----------------------------------------------------
"""
lista_ordenada = []

# print(f'\n\n\n\n evento: {evento}')

for i in range(qtd_classes):
    for j in range(len(aulas)):
        if idDuration[aulas[j]]["resourceReference"][0] == evento['gr_Classes'][i]:
            lista_ordenada.append(aulas[j])

# print(f'lista ordenada {lista_ordenada}')
"""
-----------------------------------------------------
Criando uma matriz dinamicamente de acordo com a quantidade de classes
e de acordo com a quantidade de dias lecionados em uma semana
sendo determinados pela linha_semana e coluna_semana
-----------------------------------------------------
"""

matriz_inicial = {}

for z in range(qtd_classes):
    matriz_horario = np.full((linha_semana, coluna_semana), 'aaaaaaaaaaaaa')
    matriz_inicial[z] = matriz_horario

"""
-----------------------------------------------------
Inserção dos eventos na matriz de horário utilizando a ordenação da lista_ordenada como padrão
para inserção
{0: array([['T1-S1', 'T2-S1', 'T3-S1', 'T6-S1', 'T7-S1'],
       ['T1-S1', 'T2-S1', 'T4-S1', 'T6-S1', 'T7-S1'],
       ['T1-S1', 'T2-S1', 'T4-S1', 'T6-S1', 'T7-S1'],
       ['T2-S1', 'T3-S1', 'T4-S1', 'T7-S1', 'T8-S1'],
       ['T2-S1', 'T3-S1', 'T6-S1', 'T7-S1', 'T8-S1']], dtype='<U13'), 1: array([['T1-S2', 'T2-S2', 'T3-S2', 'T5-S2', 'T6-S2'],
       ['T1-S2', 'T2-S2', 'T4-S2', 'T5-S2', 'T6-S2'],
       ['T1-S2', 'T2-S2', 'T4-S2', 'T5-S2', 'T6-S2'],
       ['T2-S2', 'T3-S2', 'T4-S2', 'T5-S2', 'T8-S2'],
       ['T2-S2', 'T3-S2', 'T5-S2', 'T6-S2', 'T8-S2']], dtype='<U13'), 2: array([['T1-S3', 'T3-S3', 'T5-S3', 'T6-S3', 'T7-S3'],
       ['T1-S3', 'T4-S3', 'T5-S3', 'T6-S3', 'T7-S3'],
       ['T1-S3', 'T4-S3', 'T5-S3', 'T6-S3', 'T7-S3'],
       ['T3-S3', 'T4-S3', 'T5-S3', 'T7-S3', 'T8-S3'],
       ['T3-S3', 'T5-S3', 'T6-S3', 'T7-S3', 'T8-S3']], dtype='<U13')}
-----------------------------------------------------
"""

# print(f' \n\n\n lista ordenada {lista_ordenada}')

try:
    for z in range(qtd_classes):
        for i in range(coluna_semana):
            for j in range(linha_semana):
                matriz_inicial[z][j][i] = lista_ordenada[x]
                # print(matriz_inicial[30][1][0])
                # print(len(matriz_inicial[z][i][j]))
                x += 1
        #print(dict_matriz)
except:
    print("Deu ruim")

dictlist = []
for key, value in matriz_inicial.items():
    temp = [value]
    dictlist.append(temp)
# print(dictlist)
# print(matriz_inicial)