# -*- decoding: utf-8 -*-

class Termino(object):
	"""docstring for Termino"""
	def __init__(self, grado, constante, variable, numero):
		super(Termino, self).__init__()
		self.grado = grado
		self.constante = constante
		self.variable = variable
		self.total = self.constante * (pow(self.variable, self.grado))
		self.numero = numero

	'''Función que suma dos términos con igual exponente'''
	def sumaTermino(self, term):
		self.constante = self.constante + term.constante

	'''Print con formato de un término '''
	def printTermino(self):
		return str(self.constante)+'a'+str(self.numero)+'('+str(self.variable)+')'+'X'+str(self.grado)