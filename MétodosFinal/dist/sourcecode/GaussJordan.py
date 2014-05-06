# -*- coding: utf-8 -*-

'''Clase que por el método de Gauss-Jordan resuleve un sistema de ecuaciones'''
class GaussJordan(object):
	"""docstring for GaussJordan"""
	def __init__(self, matriz):
		super(GaussJordan, self).__init__()
		self.matriz = matriz
		
	'''Método que multiplica toda la fila de un arreglo por un valor'''
  	def multiplicaFila(self, numero, fila):
	  	for x in xrange(0,len(self.matriz[fila])):
	  		valor = self.matriz[fila][x] * numero
	  		self.matriz[fila][x] = valor

	'''Método que resta los valores de una fila con el mismo de la columna de 
	otra fila en la misma matriz'''
	def restaFila(self, numero, fila, i):
		for x in xrange(0,len(self.matriz[fila])):
			valor = self.matriz[fila][x] - self.matriz[i][x] * numero
			self.matriz[fila][x] = valor

	'''Método que resuelve el sistema de ecuaciones'''
	def GaussJordan(self,sistema, n):
		ecuaciones = sistema
		for i in range(0,n):
			if ecuaciones[i][i] != 0:
				valor = (1 / ecuaciones[i][i])
				self.multiplicaFila(valor, i)
			for x in xrange(0,n):
				if x != i:
					self.restaFila(self.matriz[x][i], x, i)
		return self.matriz
			