# -*- coding: utf-8 -*-

class Termino(object):
	"""docstring for Termino"""
	def __init__(self, grado, constante, variable):
		super(Termino, self).__init__()
		self.grado = grado
		self.constante = constante
		self.variable = variable
		self.total = self.constante * (pow(self.variable, self.grado))

	#Función que suma dos términos con igual exponente
	def sumaTermino(self, term):
		self.constante = self.constante + term.constante