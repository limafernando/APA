import InsertionSort as IS
import SelectionSort as SS

def main():	
	
	inputList = [5, 7, 10, 4, 1, 3, 8, 6]
	outputList = []

	print('\nA entrada é: ', inputList)

	print('\nOrdenando com InsertionSort...')

	outputList = IS.InsertionSort(inputList.copy())

	print(outputList)

	print('\nOrdenando com SelectionSort...')	

	outputList = SS.SelectionSort(inputList.copy())

	print(outputList)

if __name__ == '__main__':
	main()