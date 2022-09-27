"""
Dadas las dimensiones de un bloque rectangular, calcule las diagonales de las tres
caras diferentes. Muestre el valor de la mayor diagonal.

"""

import math


x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))
z = float(input("Ingrese el valor de z: "))

caraFrontal= math.sqrt(x**2+y**2)
caraSuperior = math.sqrt(x**2+z**2)
caraLado = math.sqrt(y**2+z**2)

if caraFrontal > caraSuperior and caraFrontal>caraLado: print("cara frontal")
else: 
    if caraSuperior>caraLado: print("cara superior")
    else: print("cara de lado")
