#Laboratorio 3
#Bertha Domingo Ruiz

print "Primero numero entero"
a=int(raw_input())
print "Segundo numero entero"
y=int(raw_input())
print "Ultimo numero entero"
z=int(raw_input())
print "Los numeros enteros de menor a mayor: "
if a>=y>=z:
	print z,y,a
elif a>=z>=y:
	print y,z,a
elif y>=a>=z:
	print z,a,y
elif y>=z>=a:
	print a,z,y
elif z>=a>=y:
	print y,a,z
elif z>=y>=a:
	print a,y,z
