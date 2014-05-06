# -*- decoding: utf-8 -*-
from Termino import *

class Polinomio(object):
	"""docstring for Polinomio"""
	def __init__(self, orden, exponenteInicial):
		super(Polinomio, self).__init__()
		self.orden = orden
		self.terminos = []
		i = 0
		for x in xrange(exponenteInicial, exponenteInicial + self.orden):
			termino = Termino(x, 1, 1, i)
			self.terminos.append(termino)
			i = i + 1

	'''Método que agrega un termino al polinomio y si ya existe el orden lo suma'''
	def agregaTermino(self, termino):
		if termino.grado > self.orden:
			self.terminos.append(termino)
		else:
			self.terminos[termino.grado].sumaTermino(termino)

	def agregaTerminoIndependiente(self,termino):
		self.terminos.append(termino)
		
	'''Método que modifica un determinado término según sus variables'''
	def modificaTermino(self, grado, constante, variable, numero):
		termino = Termino(grado,constante,variable, numero)
		self.terminos[numero] = termino

	'''Método que sustituye un determinado término con otro término'''
	def modificaTermino(self, termino):
		self.terminos[termino.numero] = termino

	def modificaVariableTermino(self, numero, variable):
		self.terminos[numero].variable = variable

	'''Print especial para ver un polinomio'''
	def printPolinomio(self):
		polinomio = ''
		for x in xrange(0,len(self.terminos)):
			polinomio = polinomio+'+'+str(self.terminos[x].printTermino())
		print polinomio
		
