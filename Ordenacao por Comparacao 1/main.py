import InsertionSort as IS
import SelectionSort as SS

def main():	
	
	outputList = []

	inputList = input('Digite a lista a ser ordenada: ')
	inputList = inputList.split(' ')
	
	for i in range(0, len(inputList)):
 		inputList[i] = int(inputList[i])

	print('\nA entrada é: ', inputList)

	print('\nOrdenando com InsertionSort...')

	outputList = IS.InsertionSort(inputList.copy())

	print(outputList)

	print('\nOrdenando com SelectionSort...')	

	outputList = SS.SelectionSort(inputList.copy())

	print(outputList)

if __name__ == '__main__':
	main()