'''
parâmetro -> necessário aprenas a lista de
entrada, dela são tirados os elementos e 
o seu tamanho
'''

def SelectionSort(inputList):
	#for tem limite superior aberto
	for i in range (0, len(inputList)):
		i_min = i #i_min = índice do menor valor

		j = i+1

		for j in range(i+1, len(inputList)):
			
			if inputList[j] < inputList[i_min]:
				#algum elemente mais a direita é menor que o menor atual
				i_min = j

		if inputList[i] != inputList[i_min]:
			#troca de posição
			aux = inputList[i]
			inputList[i] = inputList[i_min]
			inputList[i_min] = aux

	return inputList