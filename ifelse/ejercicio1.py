"""
Dados el radio y altura de un cilindro, si la altura es mayor al radio calcule y
muestre el valor del volumen del cilindro, caso contrario muestre el valor del área
del cilindro.
"""

import math

r =  float(input("Ingrese radio: "))
h =  float(input("Ingrese altura: "))

if h>r: 
    v = 2 * math.pi * r * (h+r)
    print("Volumen es: ", str(v))
else: 
    a = math.pi * math.pow(r,2) * h
    print("El area es: ", str(a))   