import InsertionSort as IS
import SelectionSort as SS

def main():
	inputList = [10,2,6,15,9,24]
	outputList = []

	print(inputList)

	outputList = IS.InsertionSort(inputList)

	print(outputList)

if __name__ == '__main__':
	main()