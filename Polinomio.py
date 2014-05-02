# -*- coding: utf-8 -*-
from Termino import *

class Polinomio(object):
	"""docstring for Polinomio"""
	def __init__(self, orden, exponenteInicial):
		super(Polinomio, self).__init__()
		self.orden = orden
		self.terminos = []
		for x in xrange(exponenteInicial, exponenteInicial + self.orden):
			termino = Termino(x, 1, 1)
			self.terminos.append(termino)

	#Método que agrega un termino al polinomio y si ya existe el orden lo suma
	def agregaTermino(self, termino):
		if termino.grado > self.orden:
			self.terminos.append(termino)
		else:
			self.terminos[termino.grado].sumaTermino(termino)

	def agregaTerminoIndependiente(self,termino):
		self.terminos.append(termino)
		

	def modificaTermino(self, grado, constante, variable):
		termino = Termino(grado,constante,variable)
		self.terminos[grado] = termino
		
