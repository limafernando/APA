'''
parâmetro -> necessário aprenas a lista de
entrada, dela são tirados os elementos e 
o seu tamanho
'''

def InsertionSort(inputList):
	pivo = None
	
	for i in range (1, len(inputList)-1):
	
		pivo = inputList[i]
		j = i - 1
	
		while j >= 0 and inputList[j] > pivo:
	
			inputList[j+1] = inputList[j]
			j = j - 1
	
		inputList[j+1] = pivo
	
	return inputList