nombres = []
edades = []
# Inicializo las listas hasta que introduzca un "*"
while True:
    nombre = input("Dime el nombre de un alumno:")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Dime su edad:")))
    if nombre == "*": break;

# Calcular la edad máxima
edad_max = max(edades)
# Alumnos mayores de edad
print("Alumnos mayores de edad")
print("=======================")
for nombre, edad in zip(nombres, edades):
    if edad >= 10:
        print(nombre)

# Alumnos mayores

print("Alumnos mayores")
print("===============")
for nombre, edad in zip(nombres, edades):
    if edad == edad_max:
        print(nombre)

