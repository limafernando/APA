import MergeSort as MS
import QuickSort as QS

def main():	
	
	inputList = [5, 7, 10, 4, 1, 3, 8, 6]
	#inputList = [3,9,12,6]
	#inputList = [3,18,6,12,9]
	outputList = []

	print('\nA entrada é: ', inputList)

	print('\nOrdenando com MergeSort...')

	MS.MergeSort(inputList.copy(), 0, len(inputList)-1)

	print('\nOrdenando com QuickSort...')	

	QS.QuickSort(inputList.copy(), 0, len(inputList)-1)

	#print(outputList)

if __name__ == '__main__':
	main()