from tkinter import Tk
from tkinter.filedialog import askopenfilename

def leArquivo():
	#<Para selecionar o arquivo por GUI#
	Tk().withdraw()
	caminhoArq = askopenfilename()
	#print(caminhoArq)
	arq = open(caminhoArq, 'r')
	conteudoArq = arq.readlines()
	#print(conteudoArq)
	arq.close()
	#Para selecionar o arquivo por GUI>

	matrizAdj, listaDeOrdem, vetorDeArvores = {}, [], []

	nNos = int(conteudoArq[0]) #para acessar a primeira linha de conteudoArq

	for i in range(0, nNos): #para inicializar a floresta (vetorDeArvores)
		vetorDeArvores.append(i)

	no1 = 65 #chr(65) == 'A'
	no2 = 66 #chr(65) == 'B'
	no2Aux = no2
	aux = nNos-1

	for i in range(1, nNos): #para ir acessando as linhas de conteudoArq a partir da segunda linha
		
		listaValores = conteudoArq[i]
		#print(listaValores)

		#<ajuste devido ao arquivo
		if '\t' in listaValores:
			listaValores = listaValores.split('\t')
			#print(listaValores)
		else:
			listaValores = listaValores.split(' ')
			#print(listaValores)
		#ajuste devido ao arquivo>

		#<ajuste devido ao arquivo
		if '\n' in listaValores:
			listaValores.remove('\n')
			#print(listaValores)
		else:
			listaValores[-1] = listaValores[-1].replace('\n', '')
			#print(listaValores)
		#ajuste devido ao arquivo>

		for j in range(0, len(listaValores)):
			chave = chr(no1) + ',' + chr(no2Aux)
			valor = int(listaValores[j])

			#print(chave, ':', valor)

			matrizAdj[chave] = valor

			no2Aux += 1

		no1 += 1
		no2 += 1
		no2Aux = no2

	
	listaDeOrdem = sorted(matrizAdj, key = matrizAdj.get)

	#print(matrizAdj)

	return matrizAdj, listaDeOrdem, vetorDeArvores

def main():
	
	solucao = []
	valorDaSolucao = 0
	
	matrizAdj, listaDeOrdem, vetorDeArvores = leArquivo()

	print('Solução Parcial:', solucao)
	
	for aresta in listaDeOrdem:
		print('\nAresta da Iteração:', aresta)

		nos = aresta.split(',')
		
		no1 = nos[0]
		indiceArvoreNo1 = ord(no1) - 65 #Ex: ord('A') == 65 -> 65 - 65 = 0
		
		no2 = nos[1]
		indiceArvoreNo2 = ord(no2) - 65

		if vetorDeArvores[indiceArvoreNo1] != vetorDeArvores[indiceArvoreNo2]: #É aresta segura/Não estão na mesma árvore
			print('É Aresta Segura')

			solucao.append(aresta)
			valorDaSolucao += matrizAdj[aresta]

			#<Atualiza as árvores
			arvoreAMudar = vetorDeArvores[indiceArvoreNo2] #qual árvore que vou atualizar

			ocorrencias = vetorDeArvores.count(arvoreAMudar) #quantos nós tem naquela árvore

			for i in range(0, ocorrencias):
				indice = vetorDeArvores.index(arvoreAMudar)
				vetorDeArvores[indice] = vetorDeArvores[indiceArvoreNo1]
			#Atualiza as árvores>

		else:
			print('Não É Aresta Segura')

		print('\nSolução Parcial:', solucao)		

	print('\nÁrvore Geradora Mínima:', solucao)
	print('Valor Da Solução:', valorDaSolucao)

if __name__ == '__main__':
	main()