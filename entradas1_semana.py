# todo: inserir tudo que esta em time na respectiva lista em TimeGroups e TimeGroup

"""
-----------------------------------------------------

Todos são metodos para se conseguem pegar algum valor necessário da entrada, seja esse valor
algum id, referencia ou nome
print(idTime) -> ['gr_Mo', 'gr_Tu', 'gr_We', 'gr_Th', 'gr_Fr']
print(idTimeGroup) -> ['gr_TimesDurationTwo']
print(idDia) -> ['Mo_1', 'Mo_2', 'Mo_3', 'Mo_4', 'Mo_5', 'Tu_1', 'Tu_2', 'Tu_3', 'Tu_4', 'Tu_5', 'We_1', 'We_2', 'We_3',
'We_4', 'We_5', 'Th_1', 'Th_2', 'Th_3', 'Th_4', 'Th_5', 'Fr_1', 'Fr_2', 'Fr_3', 'Fr_4', 'Fr_5']
print(referenceDay) -> ['gr_Mo', 'gr_Mo', 'gr_Mo', 'gr_Mo', 'gr_Mo', 'gr_Tu', 'gr_Tu', 'gr_Tu', 'gr_Tu', 'gr_Tu',
'gr_We', 'gr_We', 'gr_We', 'gr_We', 'gr_We', 'gr_Th', 'gr_Th', 'gr_Th', 'gr_Th', 'gr_Th',
'gr_Fr', 'gr_Fr', 'gr_Fr', 'gr_Fr', 'gr_Fr']
print(referenceTimeGroup) -> ['gr_TimesDurationTwo', 'gr_TimesDurationTwo', 'gr_TimesDurationTwo',
'gr_TimesDurationTwo', 'gr_TimesDurationTwo', 'gr_TimesDurationTwo', 'gr_TimesDurationTwo', 'gr_TimesDurationTwo',
'gr_TimesDurationTwo',
'gr_TimesDurationTwo', 'gr_TimesDurationTwo', 'gr_TimesDurationTwo', 'gr_TimesDurationTwo', 'gr_TimesDurationTwo',
'gr_TimesDurationTwo', 'gr_TimesDurationTwo', 'gr_TimesDurationTwo', 'gr_TimesDurationTwo', 'gr_TimesDurationTwo',
'gr_TimesDurationTwo']

-----------------------------------------------------
"""

import xhstt as xhstt
import numpy as np

idTime = []
referenceTimeGroup = []
idDia = []
referenceDay = []
idTimeGroup = []
x = 0
i = 0
teste = []
timeGroupReference = {}


for xml in xhstt.root.findall('./Instances/Instance/Times/TimeGroups/Day'):
    idTime.append(xml.attrib.get('Id'))

for xml in xhstt.root.findall('./Instances/Instance/Times/TimeGroups/TimeGroup'):
    idTimeGroup.append(xml.attrib.get('Id'))

for xml in xhstt.root.findall('./Instances/Instance/Times/Time'):
    idDia.append(xml.attrib.get('Id'))
    reference = [x.attrib.get('Reference') for x in xml.findall('TimeGroups/TimeGroup')]
    timeGroupReference[i] = reference
    i += 1
    teste = []

# print(idDia)

for xml in xhstt.root.findall('./Instances/Instance/Times/Time/Day'):
    referenceDay.append(xml.attrib.get('Reference'))

for xml in xhstt.root.findall('./Instances/Instance/Times/Time/TimeGroups/TimeGroup'):
    referenceTimeGroup.append(xml.attrib.get('Reference'))

idTimeGroup_dict = {}
time = {}
temp = []
i = 0
j = 0
# print(referenceTimeGroup[0])
for i in range(len(idDia)):
    temp.append(idDia[i])
    temp.append(referenceDay[i])
    # print(len(referenceTimeGroup[1]))
    temp.append(timeGroupReference[i])
    time[i] = temp
    temp = []
    # print(time)

# print(time)
dict_time_key = dict.fromkeys(idDia)

for i in range(len(idDia)):
    temp.append(referenceDay[i])
    # print(len(referenceTimeGroup[1]))
    temp.append(timeGroupReference[i])
    dict_time_key[idDia[i]] = temp
    temp = []
"""
____________________________________
o dicionario time guarda as informações com chaves numericas
ja dict_time_key, guarda informações com o id do dia sendo a key 'mo_1'
{0: ['Mo_1', 'gr_Mo', ['gr_TimesDurationTwo', 'gr_TimesDurationThree']], 1: ['Mo_2', 'gr_Mo', ['gr_TimesDurationTwo',
 'gr_TimesDurationThree']],
{'Mo_1': ['gr_Mo', ['gr_TimesDurationTwo', 'gr_TimesDurationThree']], 'Mo_2': ['gr_Mo', ['gr_TimesDurationTwo',
 'gr_TimesDurationThree']],
____________________________________
"""
# print(dict_time_key)

"""
-----------------------------------------------------
Inserindo o id de idTimeGroup em um diciorio com a chave e o valor iguais
facilitando futuas pesquisas
{'gr_TimesDurationTwo': 'gr_TimesDurationTwo'}
print(idTimeGroup_dict)
print(idTimeGroup)
#
for i in range(len(time)):
    if not time[i][2]:
        print("ta vazio")
-----------------------------------------------------
"""

for i in idTimeGroup:
    idTimeGroup_dict[i] = idDia
#
# print(idTimeGroup)
# print(idTimeGroup_dict)

"""
-----------------------------------------------------
Criação dinamica das chaves do dicionario dos dias da semana, ja que podem variar
após essa criação, são inseridos os horarios que serão lecionados naquele dia

print(my_dict) -> {'gr_Mo': 5, 'gr_Tu': 5, 'gr_We': 5, 'gr_Th': 5, 'gr_Fr': 5}

De acordo com a quantidade de horarios letivos naquele dia, são inserir os horarios letivos
Na lista_horario, são inseridos os horario de acordo com a quantidade de dias e então ela inteira
é inserida em um dicionario com a chave representando aquele dia

print(dict_keys) -> {'gr_Mo': ['Mo_1', 'Mo_2', 'Mo_3', 'Mo_4', 'Mo_5'], 'gr_Tu': 
print(lista_horario) - > ['Mo_1', 'Mo_2', 'Mo_3', 'Mo_4', 'Mo_5']
-----------------------------------------------------
"""

dict_keys = dict.fromkeys(idTime)


my_dict = {i: referenceDay.count(i) for i in referenceDay}
lista_horario = []
y = 0
for j in range(len(dict_keys)):
    lista_horario = []
    for i in range(my_dict[idTime[j]]):
        lista_horario.append(idDia[y])
        y += 1
    dict_keys[idTime[j]] = lista_horario

coluna_semana = len(idTime)
linha_semana = len(idDia)//coluna_semana

"""
-----------------------------------------------------
Montagem das matrizes de horario propriamente dita, primeiro é criado dinamicamente uma matriz
de strings e então são inseridos na matriz_horarioS1. respeitando se aquele horario referencia o dia
em questão
print(matriz_horarioS1) -> 
[['Mo_1' 'Tu_1' 'We_1' 'Th_1' 'Fr_1']
 ['Mo_2' 'Tu_2' 'We_2' 'Th_2' 'Fr_2']
 ['Mo_3' 'Tu_3' 'We_3' 'Th_3' 'Fr_3']
 ['Mo_4' 'Tu_4' 'We_4' 'Th_4' 'Fr_4']
 ['Mo_5' 'Tu_5' 'We_5' 'Th_5' 'Fr_5']]
-----------------------------------------------------
"""

matriz_horarioS1 = np.full((linha_semana, coluna_semana), 'aaaaaaaaaaaaaa')


for i in range(coluna_semana):
    for j in range(linha_semana):
        if (idTime[i] == referenceDay[x]):
            matriz_horarioS1[j][i] = idDia[x]
            x += 1

# print(matriz_horarioS1)
