import math

global tamHeap

def MaxHeapify(inputList, i):
	esq = FilhoEsquerdo(i)
	dire = FilhoDireito(i)
	maior = i
	print("\ni:", i, " esq:", esq, " dir:", dire)
	print(inputList)
	
	#if esq < tam para validar a existencia do nó
	if esq < tamHeap and inputList[esq] > inputList[maior]:
		maior = esq
	if dire < tamHeap and inputList[dire] > inputList[maior]:
		maior = dire
	if maior != i:
		inputList[i], inputList[maior] = inputList[maior], inputList[i]
		print(inputList)
		print('\nRecursão...')
		MaxHeapify(inputList, maior)

def BuildMaxHeap(inputList):
	global tamHeap
	
	print('\nGarantindo HeapMax!')
	tamHeap = len(inputList)

	iterator = math.floor(len(inputList)/2) - 1
	for i in range(iterator, -1, -1):
		print('\nChamando MaxHeapify para o índice', i)
		MaxHeapify(inputList, i)

	print('\nTemos o HeapMax!')

def HeapSort(inputList):
	global tamHeap

	BuildMaxHeap(inputList)
	
	print('\nFazendo a ordenação!!!')

	print('\nTamanho do Heap:', tamHeap)

	for i in range(len(inputList) - 1, 0, -1):
		print('\nÍndice do laço:', i,'\n')
		print(inputList)
		print('Trocando o maior elemento, índice 0, pelo de índice', i)
		inputList[0], inputList[i] = inputList[i], inputList[0]
		print(inputList)
		tamHeap -= 1
		print('\nTamanho do Heap:', tamHeap)
		
		#se só tem um elemento na heap ele já está ordenado
		if tamHeap == 1:
			print('\nFim!!!')
			print('Array ordenado:', inputList)
		else:
			print('\nRefazendo o HeapMax!')
			MaxHeapify(inputList,0)

def FilhoEsquerdo(i):
	return (2*i + 1)

def FilhoDireito(i):
	return (2*i + 2)