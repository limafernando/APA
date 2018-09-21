from tkinter import Tk
from tkinter.filedialog import askopenfilename

'''def leArquivo():
	#Para selecionar o arquivo por GUI#
	Tk().withdraw()
	caminhoArq = askopenfilename()
	print(caminhoArq)
	arq = open(caminhoArq, 'r')
	conteudoArq = arq.readlines()
	print(conteudoArq)
	arq.close()
	#Para selecionar o arquivo por GUI#

	return matrizAdj, listaDeOrdem, vetorDeArvores
	pass'''

def leArquivo():
	matrizAdj = {'A,B':23, 'A,C':17, 'A,D':19, 'B,C': 22, 'B,D':20, 'C,D':25}
	listaDeOrdem = sorted(matrizAdj, key = matrizAdj.get)
	vetorDeArvores = [0,1,2,3] #[A,B,C,D]
	return matrizAdj, listaDeOrdem, vetorDeArvores

def main():
	
	solucao = []
	valorDaSolucao = 0
	
	matrizAdj, listaDeOrdem, vetorDeArvores = leArquivo()

	for aresta in listaDeOrdem:
		print('Solução Parcial:', solucao)

		nos = aresta.split(',')
		
		no1 = nos[0]
		indiceArvoreNo1 = ord(no1) - 65 #Ex: ord('A') == 65 -> 65 - 65 = 0
		
		no2 = nos[1]
		indiceArvoreNo2 = ord(no2) - 65

		if vetorDeArvores[indiceArvoreNo1] != vetorDeArvores[indiceArvoreNo2]: #É aresta segura
			solucao.append(aresta)
			valorDaSolucao += matrizAdj[aresta]

			#Atualiza as árvores
			ocorrencias = vetorDeArvores.count(vetorDeArvores[indiceArvoreNo2]) #quantos nós tem naquela árvore

			valorAMudar = vetorDeArvores[indiceArvoreNo2] #qual árvore que vou atualizar

			for i in range(0, ocorrencias):
				indice = vetorDeArvores.index(valorAMudar)
				vetorDeArvores[indice] = vetorDeArvores[indiceArvoreNo1]

		else:
			#done/finish it
			print('Árvore Geradora Mínima:', solucao)
			print('valor Da Solução:', valorDaSolucao)
			break

if __name__ == '__main__':
	main()