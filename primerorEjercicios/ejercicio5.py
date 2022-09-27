nombre = input("Ingrese su nombre y apellido: ")
dni = input("Ingrese DNI: ")
sueldo = input("ingrese sueldo básico: ")
antiguedad = input("Ingrese años de antiguedad: ")
estadoCivil = input("Ingrese estado civil (1 si esta casado, 0 si es soltero): ")
nroHijos = input("Numeros de hijos : ")
presentismo = input("Ingrese presentismo (1 si corresponde cobrar, 0 si no cobra): ")
MP = 200
JB = float(sueldo) * 0.11
OB = float(sueldo) * 0.03
AG = float(sueldo) * 0.01
sueldoFinal = (float(sueldo)* 0.012) * float(antiguedad) + float(sueldo) + MP * float(presentismo) - JB - OB - AG + 800 * float(estadoCivil)+ 400 * int(nroHijos)

print("Empleado: " + nombre)
print("DNI: " + dni)
print("El sueldo neto es: $" + str(sueldoFinal))
