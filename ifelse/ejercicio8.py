"""
Dadas las tres calificaciones de dos estudiantes. La calificación final de cada uno
es la suma de sus dos mejores calificaciones. Muestre un mensaje que indique cual
estudiante (1 o 2) tiene la mayor calificación final.
"""

def calcNotaFinal():
    notaFinal = 0
    for i in range(1,3):
        nota = float(input("Ingrese la calificacion"+" "+ str(i)+": "))
        notaFinal+= nota
    print("Nota final: "+ str(notaFinal))
    return notaFinal

print("Estudiante 1")
est1 = calcNotaFinal()
print("Estudiante 2")
est2 = calcNotaFinal()

if est1 == est2:
    print("Ambos estudiantes sacaron la misma calificacion final")
elif est1 > est2:
    print("El estudiante 1 tiene la mayor calificacion final")
else: 
    print("El estudiante 2 tiene la mayor calificacion final")
