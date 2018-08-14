'''
Em python o limite superior é aberto, 
por isso as somas para acessar as listas
corretamente.

A biblioteca math contêm os métodos de piso e infinito.
'''

import math as math

def MergeSort(inputList, ini, fim):
	if ini < fim:
		print('Chamada do MergeSort com a lista', inputList[ini : fim+1])
		q = math.floor((ini + fim)/2)
		print('q =', inputList[q])
		MergeSort(inputList, ini, q)
		MergeSort(inputList, q+1, fim)
		Merge(inputList, ini, q, fim)

def Merge(inputList, ini, q, fim):
	print('Chamada do Merge com a lista', inputList[ini : fim+1])
	esq = inputList[ini : q+1]
	dire = inputList[q+1 : fim+1]
	esq.append(math.inf)
	dire.append(math.inf)
	print('esq:', esq)
	#print(inputList[q])
	print('dire:', dire)
	i, j = 0, 0
	print('Entrando no for para ordenação...')
	for k in range(ini, fim+1):
		if esq[i] < dire[j]:
			inputList[k] = esq[i]
			i += 1
		else: #esq[i] >= dire[j]
			inputList[k] = dire[j]
			j += 1


		print(inputList)