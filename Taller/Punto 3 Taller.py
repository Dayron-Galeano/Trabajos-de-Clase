# Construir un programa que lea un entero positivo n y determine si dicho número es un cuadrado de otro entero, o sea, que tiene raíz cuadrada entera
n = int(input("Ingrese un número entero positivo: "))
if n > 0:
    p = n ** 0.5
    ent = int(p)
    res = p - ent
    if res == 0:
        print(f"{n} es el cuadrado de {ent}")
    else:
        print(f"{n} no es el cuadrado de algún entero")
#se saca la raíz de n, luego ent es la parte entera del resultado de la raíz, luego se resta ese resultado(p) con ent, si el resultado es igual a 0 significa que si tiene raiz entera