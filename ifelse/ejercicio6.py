"""
Lea la cantidad de Kw que ha consumido una familia y el precio por Kw. Si la
cantidad es mayor a 700, incremente el precio en 5% para el exceso de Kw sobre
700. Muestre el valor total a pagar.
"""
kwConsumido = float(input("Ingrese la cantidad de KW consumido: "))
preciokw = 4
total = kwConsumido * preciokw

if kwConsumido > 700:
    total += total * .05 
    print("Monto total a pagar: ", str(total))
else:
       print("Monto total a pagar: ", str(total))
