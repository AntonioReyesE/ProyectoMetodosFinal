# -*- coding: utf-8 -*-
from polinomio import *
from Termino import *
from Lector import *
'''Clase que implementa los métodos necesarios para 
	hacer aproximaciones por mínimos cuadrados'''

class MinimosCuadrados(object):

	def __init__(self, orden):
		super(MinimosCuadrados, self).__init__()
		self.polinomios = []
		self.orden = orden
		lec = Lector('archivo.txt')
		self.valores = lec.lee()

	def calculaSumatoriasX(self):
		sumatoriasX = []
		n = len(self.valores[0])
		suma = 0
		for x in xrange(0,n):
			
			for y in range(0,n):
				suma = suma + self.valores[0][x]
				sum = pow(suma,y)
			sumatoriasX.append(sum)
		return sumatoriasX

	def calculaSumatoriasXY(self, orden):
		return sumatoriasXY
		