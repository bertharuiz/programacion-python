#laboratorio 1
#Bertha Domingo Ruiz

tiempo=int(input("ingresa los segundos del viaje: "))
d=(int(tiempo/86400))
h=(int((tiempo-(d*86400))/3600))
m=(int((tiempo-(d*86400)-(h*3600))/60))
s=(int((tiempo-(d*86400)-(h*3600)-(m*60))))
print(str(d)+"dias "+str(h)+"horas "+str(m)+"minutos "+str(s)+" segundos")
