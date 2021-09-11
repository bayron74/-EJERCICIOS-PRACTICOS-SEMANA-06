#Diseñe un programa que lea la temperatura en centígrados del día e imprima el tipo de
#clima de acuerdo a la siguiente tabla. (Use condicional múltiple).

tpo=int(input("ingresa la temperatura actual"))

if tpo <=10:
	print("Frio")

elif tpo  >=10 and tpo <20:
		print("Nublado")
		
elif tpo >=21 and tpo < 30:
		print("Caluroso")
else:
	print("Tropical")
