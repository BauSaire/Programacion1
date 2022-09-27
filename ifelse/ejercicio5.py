"""
Lea un número. Determine si es entero y múltiplo de 7.
"""

num = float(input("Ingrese un numero"))

if num % 1 == 0 and num % 7 == 0:
    print("numero entero y multiplo de 7")
elif num % 1 == 0:
        print("numero entero")
elif num % 7 == 0:
        print("numero multiplo de 7")
else:
    print("El numero no es entero ni multiplo de 7")