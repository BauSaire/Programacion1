"""
Lea la cantidad de Kw que ha consumido una familia y el precio por Kw. Si la
cantidad es mayor a 700, incremente el precio en 5% para el exceso de Kw sobre
700. Muestre el valor total a pagar.
"""
kwConsumido = float(input("Ingrese la cantidad de KW consumido: "))
preciokw = 8
if kwConsumido > 700:
    excedente =  kwConsumido - 700
    kwConsumido -=  excedente
    kwConsumido*= preciokw
    excedente *= preciokw + preciokw*0.05
    kwConsumido+= excedente 
    print("Monto total a pagar: ", str(kwConsumido))
else:
    kwConsumido *=  preciokw        
    print("Monto total a pagar: ", str(kwConsumido))
