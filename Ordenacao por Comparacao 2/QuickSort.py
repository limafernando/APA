def QuickSort(inputList, ini, fim):
	if ini < fim:
		print('Chamada do QuickSort com a lista', inputList[ini : fim+1])
		q = Partion(inputList, ini, fim)
		print(inputList)
		#q é um elemento já ordenado
		QuickSort(inputList, ini, q-1)
		QuickSort(inputList, q+1, fim)

def Partion(inputList, ini, fim):
	print('Chamada do Partion com a lista', inputList[ini : fim+1])
	pivo = inputList[fim]
	i = ini - 1
	print('Entrando no for...')
	#até o penúltimo elemento pq o último é o pivô
	for j in range(ini, fim): 
		if inputList[j] <= pivo:
			i += 1
			#swap tuple
			inputList[i], inputList[j] = inputList[j], inputList[i]
		print(inputList)
	i += 1
	inputList[i], inputList[fim] = inputList[fim], inputList[i]
	return i