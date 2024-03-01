import re
import random
import numpy as np
import entradas1_restricao as restricao
import entradas1_recurso as recurso
import entradas1_semana as semana
import entradas1_evento as evento
import entrada1
from entradas1_evento import *

"""
        ----------------------------------------------------------------------------------------------------------------
        Calculo das restrições da solução enviada, neste dataset, o valor de todas as restrições são 1.
        Aqui são calculadas as restrições de professor (não pode dar aula no dia x da semana) e 
        Hhorários concorrentes: professores não podem dar aula pra turma 1 e a 2 ao mesmo tempo
        ---------------------------------------------------------------------------------------------------------------- 

"""



class Avaliacao():
    def __init__(self, dict_matriz):
        self.dict_matriz = dict_matriz

    def calcula(self):

        contador = 0

        """
        ----------------------------------------------------------------------------------------------------------------        
        Aqui embaixo é onde realiza-se a contagem dos horarios concorrentes para todos os professores
        ----------------------------------------------------------------------------------------------------------------
        """
        rodrigo = 0
        r = 0
        for tamanho in restricao.dict_teste2.values():
            rodrigo += 1
            try:
                if tamanho['Tag'] == 'AssignTimeConstraint':
                    tamanho_string = ''.join(tamanho["AppliesTo"])
                    if tamanho_string == idEventGroup[0]:
                        countTimes = 0
                        for key in idDuration.keys():
                            r = 0
                            for i in range(semana.coluna_semana):
                                for j in range(semana.linha_semana):
                                    if key == self.dict_matriz[r][i][j]:
                                        countTimes += 1

                            r += 1
                        if countTimes != semana.coluna_semana * semana.linha_semana:
                            contador += countTimes
            except:
                print("mais uma vez")
            if tamanho['Tag'] == 'AvoidUnavailableTimesConstraint':
                try:
                    for i in range(semana.coluna_semana):
                        for j in range(semana.linha_semana):
                            if semana.matriz_horarioS1[i][j] == tamanho["Times"][i]:
                                for z in range(len(self.dict_matriz)):
                                    if idDuration[self.dict_matriz[r][i][j]]['resourceReference'][1] == tamanho["AppliesTo"][0]:
                                        contador += 1
                                    #     print()
                except:
                    print("mais uma vez")

            if tamanho['Tag'] == 'SplitEventsConstraint':
                try:
                    for z in range(len(self.dict_matriz)):
                        for i in range(semana.coluna_semana):
                            for j in range(semana.linha_semana):
                                if i + 1 < semana.linha_semana-1:
                                    if self.dict_matriz[z][i][j] == self.dict_matriz[z][i][j] and self.dict_matriz[z][i + 1][j] == self.dict_matriz[z][i + 2][j]:
                                        # print(i, j, z)
                                        # print(f'primeiro: {self.dict_matriz[z][i][j]} - segundo: {self.dict_matriz[z][i + 1][j]}')
                                        contador += 1
                except:
                    print("deu ruim de novo")

            if tamanho['Tag'] == 'DistributeSplitEventsConstraint':
                for z in range(len(self.dict_matriz)):
                    for i in range(semana.coluna_semana):
                        for j in range(semana.linha_semana):
                            # print(idDuration[self.dict_matriz[r][i][j]]['course'][0])
                            if idDuration[self.dict_matriz[z][i][j]]['course'][0] == tamanho["AppliesTo"][j]:
                                if i + 1 < semana.linha_semana - 1:
                                    if self.dict_matriz[z][i][j] != self.dict_matriz[z][i + 1][j]:
                                        # print(i, j, z)
                                        # print(f'primeiro: {self.dict_matriz[z][i][j]} - segundo: {self.dict_matriz[z][i + 1][j]}')
                                        contador += 1
                                # print(tamanho["AppliesTo"][j])
                                #     print()
            if tamanho['Tag'] == 'AvoidClashesConstraint':
                try:
                    for z in range(len(self.dict_matriz)):
                        for i in range(semana.coluna_semana):
                            for j in range(semana.linha_semana):
                                if z + 1 < len(self.dict_matriz):
                                    if idDuration[self.dict_matriz[z][i][j]]['resourceReference'][1] == idDuration[self.dict_matriz[z+1][i][j]]['resourceReference'][1]:
                                        # print(i, j, z)
                                        contador += 1
                except:
                    print("De novo")

            if tamanho['Tag'] == 'LimitIdleTimesConstraint':
                try:
                    for z in range(len(self.dict_matriz)):
                        for i in range(semana.coluna_semana):
                            for j in range(semana.linha_semana):
                                if i + 1 < semana.linha_semana - 1:
                                    for k in range(1, semana.linha_semana - 2):
                                        # print(k + i)
                                        if self.dict_matriz[z][i][j] == self.dict_matriz[z][i + k][j]:
                                            # print(i, j, z)
                                            # print(f'primeiro: {self.dict_matriz[z][i][j]} - segundo: {self.dict_matriz[z][i + k][j]}')
                                            contador += 1
                except:
                    print("Afs")
            if tamanho['Tag'] == 'ClusterBusyTimesConstraint':
                for z in range(len(self.dict_matriz)):
                    for i in range(semana.coluna_semana):
                        for j in range(semana.linha_semana):
                            pass

        self.nota_avaliacao = contador
        return self.nota_avaliacao

            # soma as notas das avaliações, todas com custo 1

    def getAvaliacao(self):
        return self.nota_avaliacao


def printaRestricao():
    print(f'dicionario com as restricoes {restricao.dictConstraint}\n')