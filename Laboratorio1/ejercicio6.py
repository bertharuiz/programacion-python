#laboratorio 1
#Bertha Domingo Ruiz

print( 'calcular Massa corporal')

peso = raw_input (' Escribe tu peso: ')
altura = raw_input ('Escribe tu altura: ')
imc = (float(peso)/(float(altura)*float(altura)))*10000

print 'Su IMC es : ', imc
if imc <16:
    raw_input ('delgadez severa')
if imc <16.99 and imc >16:
    raw_input ('delgadez moderada')
if imc <24.99 and imc >18.5:
    raw_input ('normal')
if imc >25:
    raw_input ('sobrepeso')
