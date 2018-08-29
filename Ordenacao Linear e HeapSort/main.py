import CountingSort as CS
import Heap as HP

def main():	
	
	#inputList = [5, 7, 10, 4, 1, 6, 8, 3]
	#inputList = [3,9,12,6]
	#inputList = [3,18,6,12,9]
	#inputList = [5,4,3,2,1]
	#inputList = [22, 41, 18, 9, 7, 8, 7, 10]
	#inputList = [2,1,3,0,2]
	inputList = [1,16,5,30,27,17,20,2,57,3,90]
	n = len(inputList)
	outputList = [None]*n


	print('\nA entrada é: ', inputList)

	print('\nOrdenando com CountingSort...')

	CS.CountingSort(inputList.copy(), outputList, n)

	print('Lista ordenada:', outputList)

	print('\n\nA entrada é: ', inputList)
	print('\nOrdenando com HeapSort...')	

	HP.HeapSort(inputList.copy())

	#print(outputList)'''

if __name__ == '__main__':
	main()