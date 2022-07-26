import random
lista_numeros = []
# Primer recorrido para leer la lista
for indice in range(1,11):
	lista_numeros.append(random.randint(1,10))
## Segundo recorrido para mostrar el resultado
for numero in lista_numeros:
	print(numero," ",numero ** 2," ",numero ** 3)

