from itertools import groupby
import random
import numpy as np
import entrada1
import entradas1_semana as semana
import fitness
import copy
import operator
from collections import Counter
import time
from xlwt import Workbook
from datetime import datetime
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


tamanho_populacao = 10
geracoes = 10
c = 0
rng = np.random.default_rng()
random.seed(1)
pElite = (tamanho_populacao // 100) * 10
sheet = []
wb = Workbook()
coluna_excel = 0
sheet1 = wb.add_sheet('Resultados', cell_overwrite_ok=True)


def retorna_matriz():
    matriz_horario = np.full((semana.linha_semana, semana.coluna_semana), 'aaaaaaaa')
    return matriz_horario


def cria_populacao(tamanho_populacao):
    populacao_total = {}

    for i in range(tamanho_populacao):
        z = random.randint(0, 2)
        entrada_shuffle = copy.deepcopy(entrada1.matriz_inicial)
        populacao = {}
        entrada_shuffle[z] = copy.deepcopy(rng.permuted(entrada1.matriz_inicial[z]))
        nota = fitness.Avaliacao(entrada_shuffle)
        populacao[0] = copy.deepcopy(entrada_shuffle)
        populacao[1] = nota.calcula()
        populacao_total[i] = copy.deepcopy(populacao)
    return populacao_total


"""
Função para ordenação do dicionário. A ordenação é feita da menor função objetivo para a maior. 
"""


def ordena_dict(dicionario):
    aux = {}
    dic = {}
    for i in range(len(dicionario)):
        aux[i] = copy.deepcopy(dicionario[i][1])

    sorted_dic = sorted(aux.items(), key=operator.itemgetter(1))

    for i in range(len(dicionario)):
        dic[i] = dicionario[sorted_dic[i][0]]

    return dic


def crossover(parent1, parent2):
    child = copy.deepcopy(entrada1.matriz_inicial)
    z = random.randint(0, 2)
    parent1_array = list((np.asarray(parent1[z])).flatten())
    del_parent1_array = copy.deepcopy(parent1_array)
    parent2_array = list((np.asarray(parent2[z])).flatten())
    one_point = random.randint(0, len(parent1_array)//2)
    two_point = random.randint(len(parent1_array)//2, len(parent1_array))
    del del_parent1_array[one_point:two_point]
    contagem = Counter(del_parent1_array)

    for i in range(semana.coluna_semana):
        for j, k in zip(range(semana.linha_semana), range(one_point)):
            child[z][i][j] = parent1_array[k]
    for i in range(semana.coluna_semana):
        for j, k in zip(range(semana.linha_semana), range(two_point, len(parent2_array))):
            child[z][i][j] = parent1_array[k]

    for i in range(semana.coluna_semana):
        for j, k in zip(range(semana.linha_semana), range(one_point, two_point)):
            if parent1_array[k] not in contagem:
                child[z][i][j] = parent2_array[k]
            else:
                contagem[parent2_array[k]] -= - 1
                if contagem[parent2_array[k]] < 0:
                    child[z][i][j] = parent2_array[k]
    return child


def retorna_elite(dic_ordenado):
    elite = {}
    for i in range(pElite+1):
        elite[i] = dic_ordenado[i]
    return elite


def mutation(child):
    z = random.randint(0, 2)
    filho = {}
    filhos = {}
    while True:
        rand = float("%.4f" % random.random())
        if rand <= 0.1:
            child[z] = copy.deepcopy(rng.permuted(child[z]))
            filho[0] = copy.deepcopy(child)
            nota = fitness.Avaliacao(child).calcula()
            filho[1] = nota
            filhos[0] = copy.deepcopy(filho)
            filhos = copy.deepcopy(ordena_dict(filhos))
            return filhos


def cria_geracao(parents):
    filho = {}
    filhos = {}
    for i in range(1, ((tamanho_populacao // 5) * 4)):
        z = random.randint(0, tamanho_populacao - 1)
        y = random.randint(0, tamanho_populacao - 1)
        filho_horario = (crossover(parents[z][0], parents[y][0]))
        nota = fitness.Avaliacao(filho_horario).calcula()
        filho[0] = copy.deepcopy(filho_horario)
        filho[1] = nota
        filhos[i] = copy.deepcopy(filho)
    return filhos


def cria_mutante(mut):
    for z in range(len(mut)):
        mut[((tamanho_populacao//5)*4)+pElite] = mutation(mut[z][0])
    print(f'\n\n\n\n mut {mut}')
    print(f'\n\n\n\n mut {len(mut)}')
    return mut


def escreve_excel(t_total, solucao, populacao, geracao):
    sheet1.write(0, 0, 'Populacao')
    sheet1.write(0, 1, 'Geracao')
    sheet1.write(0, 2, 'Solucao')
    sheet1.write(0, 3, 'Tempo')
    sheet.append(populacao)
    sheet.append(geracao)
    sheet.append(solucao)
    sheet.append(t_total)
    j = 1
    for x in range(4):
        sheet1.write(1, 0, populacao)
        sheet1.write(1, 1, geracao)
        sheet1.write(1, 2, solucao)
        sheet1.write(1, 3, t_total)

    today = datetime.today()
    # dd/mm/YY
    d1 = today.strftime("%d-%m-%Y")
    wb.save(f'Resultados_' + d1 + '.xls')



def main():
    parent = random.randint(0, tamanho_populacao)
    populacao_total = cria_populacao(tamanho_populacao)
    filho_horario = {}
    geracao = {}
    filho = {}
    filhos = {}
    # for i in populacao_total.values():
    #     print(f'\n{i[0]}')
    dic_ordenado = ordena_dict(populacao_total)
    filhos = retorna_elite(dic_ordenado)
    for j in range(geracoes):
        for i in range(1, ((tamanho_populacao//5)*4)):
            z = random.randint(0, tamanho_populacao-1)
            y = random.randint(0, tamanho_populacao-1)
            filho_horario = (crossover(dic_ordenado[z][0], dic_ordenado[y][0]))
            # print(f'\n\n filho: {filho_horario}')
            nota = fitness.Avaliacao(filho_horario).calcula()
            filho[0] = copy.deepcopy(filho_horario)
            filho[1] = nota
            filhos[i] = copy.deepcopy(filho)
        filho_ornedado = ordena_dict(filhos)
        # dic_ordenado = copy.deepcopy(filho_ornedado)
        elite = copy.deepcopy(filho_ornedado[0])
        filhos = retorna_elite(filho_ornedado)
        # dic_ordenado = {**filhos, **filho_ornedado, **cria_mutante(filho_ornedado)}
        # print(len(dic_ordenado))
        # elite = copy.deepcopy(filho_ornedado[0])
        geracao[j] = filho_ornedado

    # print(f'\n\n geracao: {geracao[0][0]}\n\n')
    # print(f'\n\n geracao: {geracao[9][0]}\n\n')
    filho_ornedado = ordena_dict(filhos)
    for z in range(len(filho_ornedado)):
        filho_ornedado[((tamanho_populacao//5)*4)+1] = mutation(filho_ornedado[z][0])
    return geracao[0][0]


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    start_time = time.time()
    melhor = main()
    total_time = time.time() - start_time
    print("--- %s seconds ---" % (time.time() - start_time))
    escreve_excel(total_time, melhor[1], tamanho_populacao, geracoes)
