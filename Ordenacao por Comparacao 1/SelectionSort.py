def SelectionSort(inputList):
	for i in range (0, len(inputList)-1):
		min_index = i

		j = i+1

		for j in range(i+1, len(inputList)-1):
			if inputList[j] < inputList[min_index]:
				min_index = j

		if inputList[i] != inputList[min_index]:
			#troca de posição
			temp = inputList[i]
			inputList[i] = inputList[min_index]
			inputList[min_index] = temp

	return inputList