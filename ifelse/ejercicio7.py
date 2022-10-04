"""
Lea un valor de temperatura t y un código p que puede ser 1 o 2. Si el código es 1
convierta la temperatura t de grados f a grados c con la fórmula c=5/9(t-32). Si el
código es 2 convierta la temperatura t de grados c a f con la fórmula: f=32+9t/5,
caso contrario muestre un mensaje de error.
"""


t= float(input("Ingrese la temperatura: "))
cod = int(input("Ingrese 1 para convertir a grados F a C y 2 para convertir a grados C a F: "))

if cod == 1:
    t = 5/9(t-32)
elif cod == 2:
    t = 32+9*t/5
else: print("No se renoce el codigo")

print( str(t)+ "°")