import MergeSort as MS
import QuickSort as QS

def main():	
	
	#inputList = [5, 7, 10, 4, 1, 6, 8, 3]
	#inputList = [3,9,12,6]
	#inputList = [3,18,6,12,9]
	#inputList = [5,4,3,2,1]
	inputList = [22, 41, 18, 9, 8, 7, 10]
	outputList = []

	print('\nA entrada é: ', inputList)

	print('\nOrdenando com MergeSort...')

	MS.MergeSort(inputList.copy(), 0, len(inputList)-1)

	print('\n\nA entrada é: ', inputList)
	print('\nOrdenando com QuickSort...')	

	QS.QuickSort(inputList.copy(), 0, len(inputList)-1)

	#print(outputList)

if __name__ == '__main__':
	main()