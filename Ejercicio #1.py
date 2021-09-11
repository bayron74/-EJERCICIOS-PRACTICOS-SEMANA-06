#Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el
#día de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la
#compra. Visualizar el descuento y el total a pagar por la compra.

mt = int(input("Ingrese el monto"))
dia = input("Ingrese el dia de hoy")

if dia ==("martes") and ("jueves"):
    descuento = mt * 0.15
    total = mt - descuento
    print("Su descuento es:", descuento)
    print("El total a pagar es:",total)
    
else:
    print("Su total a pagar es:", mt)
    
    



