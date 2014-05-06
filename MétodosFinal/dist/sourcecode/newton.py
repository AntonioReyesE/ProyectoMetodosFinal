# -*- encoding: utf-8 -*-
import math
#Clase que implementa los métodos necesarios para solucionar por el método de Newton
class newton:

	k = 0  #El orden 
	lista = [] #La lista que guarda los valores iniciales y los generados a partir de ellos
	intervalo = 0 #La diferencia general entre los valores de x
	xAnterior = 0 #La x0 de la formula de Newton


	#Contructor de la clase que inicializa la matriz
	def __init__(self, matriz):
		#Matriz que recibe a partir de archivo leido
		self.matriz = matriz
		self.intervalo()
		#self.DiferenciasFinitas()

	#Primera forma de calcular las diferencias finitas de la función tabular
	#Regresa el orden de la función
	def DiferenciasFinitas(self):
		lista = []
		y = self.matriz[1] #Obtenr el valor de la tabulación en y
		lista.append(self.matriz[0])
		lista.append(y)
		igual = self.iguales(y) #Para la primera comparación
		if igual != False:
			print "false"
			return False
		else:
		
			#Hasta que todos los valores del arreglo sean iguales
			k = 0
			while igual != True:
				k = k + 1
				i = 0
				j = 1
				resultado = []
				#resta de los valores de y
				while j < len(y):
					resta = float(y[j]) - float(y[i])
					i = i + 1
					j = j + 1
					resultado.append(resta)
				igual = self.iguales(resultado)
				y = resultado
				lista.append(resultado)
			self.k = k
			self.lista = lista
			print "true"
			return True


	#Función que identifica si todos los elementos de un arreglo son iguales
	def iguales(self,resultado):
		f = resultado[0]
		for x in xrange(0,len(resultado)):
			if resultado[x] != f:
				return False	
		return True

	#La primera función a llamar para hacer la validación principal
	#Función que detecta si h es constante, y si lo es regresa la distancia, sino regresa -1
	def intervalo(self):
		i = 0
		j = 1
		resta = abs(abs(float(self.matriz[0][j])) - abs(float(self.matriz[0][i])))
		while j < len(self.matriz[0]):
			resta2 = abs(abs(float(self.matriz[0][j])) - abs(float(self.matriz[0][i])))
			i = i + 1
			j = j + 1
			if(resta != resta2):
				self.intervalo = -1
				return -1
		self.intervalo = resta
		return resta

	#Función que calcula la k y pone xAnterior
	def fraccionIntervalo(self,x0):
		valor = float(self.matriz[0][0])
		if valor == x0:
			valor = x0
		elif x0 % self.intervalo == 0:
			valor = x0
		elif x0 > valor:
			while valor < x0:
				valor = valor + self.intervalo
			valor = valor - self.intervalo
		elif x0 < valor:
			while x0 < valor:
				valor = valor - self.intervalo
			valor = valor + self.intervalo
		fraccIn = (x0 - valor) / self.intervalo
		self.xAnterior = valor
		return fraccIn

	#Función que resuleve la interpolacion ya generada de newton
	def formula(self, xUsuario, orden):
		
		k = self.fraccionIntervalo(xUsuario)
		if(orden<self.k):
			self.k = orden

		self.extrapolacion(self.xAnterior) #aqui ta extrapolacion 
		indice = self.lista[0].index(self.xAnterior)
		res = 1
		y0 = self.lista[1][indice]
		for i in range (self.k,0,-1):
			for j in range(0, i):
				res = res * (k - j)
			res = (res * self.lista[j+2][indice]) / math.factorial(j+1)
			y0 = y0 + res
			res = 1
		print ""
		print " El orden del Polinomio que más se ajusta " + str(self.k)
		print " El metodo para extrapolar/interpolar usado fue Newton"
		print " El resultado de la aproximación es "  + str(y0)

	#Función que extrapola según un valor dado válido de acuerdo al intervalo
	def  extrapolacion(self, xDeseado):
		xDeseado = (3 * self.intervalo) + xDeseado
		if xDeseado < self.lista[0][0]:
			while not xDeseado in self.lista[0]:
				self.lista[-1].insert(0,self.lista[-1][0])
				for i in range(self.k, 0, -1):
					self.lista[i].insert(0, self.lista[i][0] - self.lista[i + 1][0])
				self.lista[0].insert(0, self.lista[0][0] - self.intervalo)
		else:
			while not xDeseado in self.lista[0]:
				self.lista[-1].append(self.lista[-1][-1])
				for i in range(self.k, 0, -1):
					self.lista[i].append(self.lista[i][-1] + self.lista[i + 1][-1])
				self.lista[0].append(self.lista[0][-1] + self.intervalo)
		print self.lista
			

	def kill(self):
		del self
