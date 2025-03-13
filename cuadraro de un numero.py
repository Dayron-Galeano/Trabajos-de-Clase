n = int(input("Ingrese un número entero positivo: "))
if n > 0:
    p = n ** 0.5
    ent = int(p)
    res = p - ent
    if res == 0:
        print(f"{n} es el cuadrado de {ent}")
    else:
        print(f"{n} no es el cuadrado de algún entero")