# -*- decoding: utf-8 -*-
from MinimosCuadrados import *
from Lector import *
from GaussJordan import *
'''Main del programa'''

minimos = MinimosCuadrados(3)

lec = Lector("archivo.txt")
m = lec.lee()

var = minimos.formatearEcuaciones()

matriz = minimos.transfomaEcuaciones(var)

print matriz

gauss = GaussJordan(matriz)
m = gauss.GaussJordan(matriz, 3)
print m

n = minimos.obtenerResultados(m)

p = minimos.arregloPolinomio(n)

p.printPolinomio()