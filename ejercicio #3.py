#Hacer un programa que simule un cajero automatico que solamnente pueda retirar multiplos de 5 "UTILZAR EL OPERADOR Mod"
#si el dato es multiplo de 5 entrgar dinero pero si el ddato ingresado no es multiplo de 5 mostrar
#un mensaje error

dt = int(input("Ingrese la cantidad de dinero a sacar"))
ml = 5

if dt == ml:
    cr = dt % ml
    print("su residuo", cr )

else:
    print("Error")

#Hasta aca llegamos, pude lo que pude lic, pero no le encontre mas cobertura
