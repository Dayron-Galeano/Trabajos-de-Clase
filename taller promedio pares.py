n = int(input("Ingrese el número de datos que va a poner: "))
i = 1
res = 0
np = 0
while i <= n:
    dato = int(input("Ingrese el valor: "))
    if dato % 2 == 0:
        res = res + dato
        np = np + 1
    i += 1
print(res/np)
