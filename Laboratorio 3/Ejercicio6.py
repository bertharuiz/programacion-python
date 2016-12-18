#Laboratorio 3
#Bertha Domingo Ruiz

a=input("Agrega tu edad para convertirlos en años perro")
while a<0:
    print "No hay edades negativas"
    a=input("Agrega tu edad para convertirlos en años perro")
if a<2:
    p=a*10.5
if a>=2:
    p=((a-2)*4)+21.0
print  p, "años perro"
