# -*- decoding: utf-8 -*-
from MinimosCuadrados import *
from Lector import *
from GaussJordan import *
from newton import *
import math

lec = Lector("archivo.txt")
m = lec.lee()

print "Hola, este programa obtiene una función polinomial a partir de una función tabular"

newt = newton(m)
a = newt.intervalo
if  a != -1:
	print "Los incrementos no son constantes, favor de ingresar el orden deseado"
	orden = int(raw_input("Favor de introducir el orden"))
	if orden > len(m) - 1:
		orden = len(m) - 1
	minimos = MinimosCuadrados(orden)

	print "Las ecuaciones: "
	var = minimos.formatearEcuaciones()
	matriz = minimos.transfomaEcuaciones(var)

	for x in xrange(0,len(var)):
		print var[x].printPolinomio()

	gauss = GaussJordan(matriz)
	m = gauss.GaussJordan(matriz, orden)

	n = minimos.obtenerResultados(m)
	p = minimos.arregloPolinomio(n)

	print "Resultado: "
	p.printPolinomio()
else:
	newt.DiferenciasFinitas()
	orden = newt.k + 1
	minimos = MinimosCuadrados(orden)

	print "Las ecuaciones: "
	var = minimos.formatearEcuaciones()
	matriz = minimos.transfomaEcuaciones(var)

	for x in xrange(0,len(var)):
		print var[x].printPolinomio()

	gauss = GaussJordan(matriz)
	m = gauss.GaussJordan(matriz, orden)

	n = minimos.obtenerResultados(m)
	p = minimos.arregloPolinomio(n)

	print "Resultado: "
	p.printPolinomio()

