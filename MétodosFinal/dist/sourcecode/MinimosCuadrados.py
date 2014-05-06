# -*- decoding: utf-8 -*-
from Polinomio import *
from Termino import *
from Lector import *
'''Clase que implementa los métodos necesarios para 
	hacer aproximaciones por mínimos cuadrados'''

class MinimosCuadrados(object):

	def __init__(self, orden):
		super(MinimosCuadrados, self).__init__()
		self.polinomios = []
		self.orden = orden + 1
		lec = Lector('archivo.txt')
		self.valores = lec.lee()

		'''Método que calcula las sumatorias de x en las potencias según el orden
		y las regresa en un arreglo'''
	def calculaSumatoriasX(self, i):
		sumatoriasX = []
		n = len(self.valores[0])
		suma = 0
		for x in xrange(0,i):
			suma = 0
			for y in range(0 , n):
				suma = suma + pow(self.valores[0][y], x)
			sumatoriasX.append(suma)
		return sumatoriasX

		'''Método que calcula la sumatoria de xi*yi para los exponentes necesarios 
		dado un orden'''
	def calculaSumatoriasXY(self):
		sumatoriasXY = []
		n = len(self.valores[0])
		suma = 0
		for x in xrange(0, n - 1):
			suma = 0
			for y in range(0 , n):
				suma = suma + pow(self.valores[0][y], x) * self.valores[1][y]
			sumatoriasXY.append(suma)
		return sumatoriasXY

		'''Método que crea el sistema de ecuaciones necesario para 
		la resolución'''
	def creaEcuaciones(self):
		ecuaciones = []
		n = self.orden
		for x in xrange(0,n - 1):
			pol = Polinomio(self.orden, x)
			ecuaciones.append(pol)
		return ecuaciones

		'''Método que da formato a las ecuaciones para el sistema'''
	def formatearEcuaciones(self):
		ecuaciones = self.creaEcuaciones()
		sumatoriasX = self.calculaSumatoriasX(ecuaciones[-1].terminos[-1].grado)
		sumatoriasXY = self.calculaSumatoriasXY()
		inicial = 0
		for x in xrange(0,len(ecuaciones)):
			val = inicial
			for y in range(0, len(ecuaciones[x].terminos) - 1):
				ecuaciones[x].modificaVariableTermino(y, sumatoriasX[val]);
				val = val + 1
			ecuaciones[x].modificaVariableTermino(-1, -1 * sumatoriasXY[inicial]);
			inicial = inicial + 1
		return ecuaciones

	'''Método que toma los terminos del sistema de ecuaciones y los convierte
	a una matriz'''
	def transfomaEcuaciones(self, ecuaciones):
		matriz = []
		for x in xrange(0,len(ecuaciones)):
			elementos = []
			for y in range(0, ecuaciones[x].orden):
				elementos.append(ecuaciones[x].terminos[y].variable)
			matriz.append(elementos)
		return matriz

	'''Método que regresa en una matriz los resultados de un sistema de ecuaciones'''
	def obtenerResultados(self, matriz):
		resultados = []
		res = len(matriz)
		for x in xrange(0,len(matriz)):
			resultados.append(matriz[x][res])
		return resultados

		'''Método que convierte un arreglo en orden a un polinomio'''	
	def arregloPolinomio(self, arreglo):
		polinomio = Polinomio(len(arreglo),0)
		for x in xrange(0,len(arreglo)):
			polinomio.modificaVariableTermino(x,arreglo[x] * -1)
		return polinomio

			
		