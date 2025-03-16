#Construir un programa que muestre el siguiente término de la serie de Fibonacci respecto a un valor entero dado por el usuario
n = int(input("Ingrese un número: "))
penultimo = 0
ultimo = 1
suma = ultimo + penultimo
while ultimo < n:
    penultimo = ultimo
    ultimo = suma
    suma = ultimo + penultimo
suma = ultimo + penultimo
print(suma)