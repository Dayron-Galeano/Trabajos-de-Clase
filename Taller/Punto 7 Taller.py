# Escribir un programa que determine si un número entero es positivo, negativo o cero. Después, modificar el programa para que reciba entradas de números enteros hasta que el número introducido sea 0. El programa debe dar el conteo de positivos y negativos y los respectivos promedios.
n = int(input("Ingrese un número entero : "))
Positivos = 0
Negativos = 0
Pvalores = 0
Nvalores = 0
while n != 0:
    if n > 0:
        Positivos = Positivos + 1
        Pvalores = Pvalores + n
        print(f"{n} es positivo")
    elif n < 0:
        Negativos = Negativos + 1
        Nvalores = Nvalores + n
        print(f"{n} es negativo")
    n = int(input("Ingrese un número entero : "))
if n == 0:
    Pmedia = Pvalores/Positivos
    Nmedia = Nvalores/Negativos
    print("El numero es 0")
    print(f"Hay {Positivos} números positivos")
    print(f"Hay {Negativos} números negativos")
    print(f"La media de los números positivos es {Pmedia}")
    print(f"La media de los números negativos es {Nmedia}")





