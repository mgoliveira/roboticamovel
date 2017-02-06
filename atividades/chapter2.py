#coding: utf-8

import numpy as np

def sin(seno):

	sin = np.sin(seno)
	return sin
	

def cos(cosseno):

	cos = np.cos(cosseno)
	return cos


def wagner():
	
	''' Escrevendo um ponto que está em relação a um eixo local em relação ao eixo origem '''
	
	# Variáveis do ponto em relação ao eixo local
	LxP = int(input('Informar o x do ponto em relação ao eixo local: ')) # x
	LyP = int(input('Informar o y do ponto em relação ao eixo local: ')) # y
	
	# Variáveis do eixo local em relação ao origem
	OxL = int(input('Informar o x do eixo local em relação ao eixo origem: ')) # x
	OyL = int(input('informar o y do eixo local em relação ao eixo origem: ')) # y
	OtetaL = int(input('Informar o angulo teta do eixo local em relação ao eixo origem: ')) # teta

	# Matriz do ponto em relação ao eixo local
	Lp = np.matrix([[LxP], [LyP], [1]])
	# Matriz de rotação e translação do eixo local em relação ao eixo origem	
	OrL = np.matrix([[cos(OtetaL), sin(OtetaL), OxL], [sin(-OtetaL), cos(OtetaL), OyL], [0, 0, 1]])

	# Escrevendo o ponto em relação ao eixo origem
	Op = np.matmul(OrL, Lp)	

  # Mostrando pose do ponto em relação ao eixo origem
	print(Op)

if __name__ == "__main__":
    	wagner()
