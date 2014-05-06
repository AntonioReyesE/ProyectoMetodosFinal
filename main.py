# -*- decoding: utf-8 -*-
from MinimosCuadrados import *
from Lector import *
from GaussJordan import *
from newton import *

lec = Lector("archivo.txt")
m = lec.lee()

newton = newton(m)
newton.DiferenciasFinitas()
orden = newton.k + 1
minimos = MinimosCuadrados(orden)

print "Las ecuaciones: "

var = minimos.formatearEcuaciones()

print len(var[0].terminos)

matriz = minimos.transfomaEcuaciones(var)

print matriz

gauss = GaussJordan(matriz)
m = gauss.GaussJordan(matriz, orden)
print m

n = minimos.obtenerResultados(m)

p = minimos.arregloPolinomio(n)

p.printPolinomio()

