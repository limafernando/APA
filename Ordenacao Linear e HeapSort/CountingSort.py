#inputList = A[]; outputList = B[];
# k = tamanho do intervalo; n = tamanho de A[];

def CountingSort(inputList, outputList, n):
	
	k = findRange(inputList)
	print('\nO intervalo vai de 0 à', k-1)
	
	auxList = []
	
	for i in range(0, k):
		auxList.append(0)

	print('\nArray auxiliar após iniciado com', k,'índices:', auxList)

	for i in range(0, n):
		auxList[inputList[i]] += 1
	
	print('\nArray auxiliar após contagem dos elementos no array de entrada:', auxList)
	
	for i in range(1, k):
		auxList[i] += auxList[i-1]
	
	print('\nArray auxiliar após contagem dos elementos anteriores ao elemento de índice i:', auxList)
	
	for i in range(n-1, -1, -1): #vai de n-1 até 0
		print('\nA[', i,']:', inputList[i], '(valor a ser ordenado) '
			+ '| C[', inputList[i],']:', auxList[inputList[i]], '(índice-1 para B)')
		print('Índice acessado em B[]:', auxList[inputList[i]] - 1)

		outputList[auxList[inputList[i]] - 1] = inputList[i]

		print('Ordenando:', outputList)

		auxList[inputList[i]] -= 1

		print('Array auxiliar atualizado:', auxList)


def findRange(inputList):
	maxValue = -1 #ex 3
	for i in inputList:
		if i > maxValue:
			maxValue = i
	rangeFound = maxValue+1 #ex 0 1 2 3
	return rangeFound