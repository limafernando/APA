'''
parâmetro -> necessário aprenas a lista de
entrada, dela são tirados os elementos e 
o seu tamanho
'''

def InsertionSort(inputList):
	pivo = None
	
	#for tem limite superior aberto
	for i in range(1, len(inputList)):
	
		pivo = inputList[i]
		j = i - 1
	
		#troca os elementos de posição
		while j >= 0 and inputList[j] > pivo:
	
			inputList[j+1] = inputList[j]
			j = j - 1
		
		#se não entrar no while não faz mudança nenhuma
		inputList[j+1] = pivo
	
	return inputList