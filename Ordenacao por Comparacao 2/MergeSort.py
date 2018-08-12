'''
Em python o limite superior é aberto, 
por isso as somas para acessar as listas
corretamente.

A biblioteca math contêm os métodos de piso e infinito.
'''

import math as math

def MergeSort(inputList, ini, fim):
	if ini < fim:
		q = math.floor((ini + fim)/2)
		MergeSort(inputList, ini, q)
		MergeSort(inputList, q+1, fim)
		Merge(inputList, ini, q, fim)
		#print(inputList)

def Merge(inputList, ini, q, fim):
	esq = inputList[ini : q+1]
	dire = inputList[q+1 : fim+1]
	esq.append(math.inf)
	dire.append(math.inf)
	i, j = 0, 0
	for k in range(ini, fim+1):
		#print(esq)
		#print(dire)
		if esq[i] < dire[j]:
			inputList[k] = esq[i]
			i += 1
		else:
			inputList[k] = dire[j]
			j += 1


		print(inputList)