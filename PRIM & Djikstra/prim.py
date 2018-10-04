from tkinter import Tk
from tkinter.filedialog import askopenfilename
from math import inf as infinito
import re

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

	matrizAdj, listaDeOrdem, vertices = {}, [], []

	nVertices = int(conteudoArq[0]) #para acessar a primeira linha de conteudoArq

	no1 = 0

	for i in range(0, nVertices): #para inicializar a floresta (vertices)
		vertices.append(no1)
		no1 += 1

	no1 = 0 
	no2 = 1 
	no2Aux = no2
	aux = nVertices-1

	for i in range(1, nVertices): #para ir acessando as linhas de conteudoArq a partir da segunda linha
		
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
			chave = str(no1) + ',' + str(no2Aux)
			valor = int(listaValores[j])

			#print(chave, ':', valor)

			matrizAdj[chave] = valor

			no2Aux += 1

		no1 += 1
		no2 += 1
		no2Aux = no2

	
	listaDeOrdem = sorted(matrizAdj, key = matrizAdj.get)

	print(matrizAdj)

	return nVertices, vertices, matrizAdj

def main():
	
	solucao = []
	valorDaSolucao = 0
	
	nVertices, vertices, adj = leArquivo()

	chave = [None]*nVertices
	pai = [None]*nVertices

	#<iniciando as chaves e vértices
	print(nVertices)
	print(vertices)
	for vertice in range(0, nVertices):
		print(vertice)
		chave[vertice] = infinito
		pai[vertice] = None

	print(vertices[0])

	chave[vertices[0]] = 0 #verticeInicial sempre é o vertice[0] == 'A'

	#iniciando as chaves e vértices>

	Q = vertices

	while Q != []:
		u = Q[0]
		regex = r'[%d]+'
		for vertice in adj[u]:
			if (vertice in Q) and (peso(u, vertice) < chave[vertice]):
				pai[v] = u
				chave[v] = peso(u, vertice)

	'''print('\nÁrvore Geradora Mínima:', solucao)
	print('Valor Da Solução:', valorDaSolucao)
'''
if __name__ == '__main__':
	main()