"""
Dados el radio y altura de un cilindro, si la altura es mayor al radio calcule y
muestre el valor del volumen, caso contrario muestre el mensaje: 'Error'

"""
import math

r =  float(input("Ingrese radio: "))
h =  float(input("Ingrese altura: "))

if h>r: 
    v = 2 * math.pi * r * (h+r)
    print("Volumen es: ", str(v))
else: 
   print("Error")