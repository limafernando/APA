import math

global tamHeap

def MaxHeapify(inputList, i):
	esq = FilhoEsquerdo(i)
	dire = FilhoDireito(i)
	maior = i
	
	if esq <= tamHeap and  inputList[esq] > inputList[maior]:
		maior = esq
	if dire <= tamHeap and  inputList[dire] > inputList[maior]:
		maior = dire
	if maior != i:
		inputList[i], inputList[maior] = inputList[maior], inputList[i]
		MaxHeapify(inputList, maior)

def BuildMaxHeap(inputList):
	global tamHeap
	
	tamHeap = len(inputList)

	iterator = math.floor(len(inputList)/2) - 1
	for i in range(iterator, -1, -1):
		MaxHeapify(inputList, i)

def HeapSort(inputList):
	global tamHeap

	BuildMaxHeap(inputList)
	for i in range(len(inputList) - 1, -1, -1):
		print(inputList[0])
		print(inputList[i])
		inputList[0], inputList[i] = inputList[i], inputList[0]
		tamHeap -= 1
		print(inputList[0])
		print(inputList[i])
		MaxHeapify(inputList,0)
	print(inputList)

	print(inputList)

def FilhoEsquerdo(i):
	return (2*i + 1)

def FilhoDireito(i):
	return (2*i + 2)