# Construir un programa que muestre los términos de la serie de Fibonacci que sean menores o iguales a un valor entero dado por el usuario
n = int(input("Ingrese el número límite: "))
penultimo = 0
ultimo = 1
print(penultimo)
print(ultimo)
suma = ultimo + penultimo
while ultimo <= n:
    print(suma)
    suma = ultimo + penultimo
    penultimo = ultimo
    ultimo = suma
    
