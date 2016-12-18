#Bertha Domingo Ruiz
#Laboratorio 3

import math
print "ingrese latitud 1:"
A1 = float(raw_input())
print "ingrese longitud 1"
A2 = float(raw_input())
print "ingrese latitud 2"
P1 = float(raw_input())
print "ingrese longitud 2"
P2 = float(raw_input())

a = (A1*math.pi)/180
b = (A2*math.pi)/180
c = (P1*math.pi)/180
d = (P2*math.pi)/180

d = 6371.01*math.acos(math.sin(a)*math.sin(c)
	    +math.cos(a)*math.cos(c)*math.cos(b-d))
print "la distancia es: ", d, "km"
