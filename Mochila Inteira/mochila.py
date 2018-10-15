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

	#print(conteudoArq)

	aux = conteudoArq[0].split('\n')
	aux = aux[0].split(' ')
	nItens = int(aux[0])
	pesoMax = int(aux[1])

	pesos = []
	valores = []

	for i in range(1, len(conteudoArq)):
		aux = conteudoArq[i].split('\n')
		aux = aux[0].split(' ')
		pesos.append(int(aux[0]))
		valores.append(int(aux[1]))

	return nItens, pesoMax, pesos, valores


def init(pesoMax, nItens):

	memo = [[None for column in range(nItens+1)] for row in range(pesoMax+1)]
	return memo

def main():
	nItens, pesoMax, pesos, valores = leArquivo()
	
	memo = init(pesoMax, nItens)
	solucao = []

	#print(memo)
	
	for w in range(0, pesoMax+1):
		for i in range(nItens + 1):
			if (w == 0 or i == 0):
				memo[w][i] = 0
			elif (w < pesos[i-1]):
				memo[w][i] = memo[w][i-1]
			else:
				memo[w][i] = max (memo[w - pesos[i-1]][i - 1] + valores[i-1], memo[w][i-1])
			'''print(memo)
			print("\n")'''
	
	print('Valor da solução:', memo[w][i])

	#Encontra os itens que foram selecionados para encontrar o valor da solucao
	for j in range(i, 0, -1):
		#print(pesoMax)
		if (memo[pesoMax][j] != memo[pesoMax][j - 1]):
			solucao.append(j)
			pesoMax -= pesos[j-1]

    #Ordena os itens que foram selecionados
	solucao.sort()

    #Apresenta os itens que foram selecionados
	print('Índice dos itens na mochila:', solucao)

if __name__ == '__main__':
	main()