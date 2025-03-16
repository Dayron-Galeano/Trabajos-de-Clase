#Construir un programa que lea dos números y si son ambos pares o ambos impares, halle el máximo común divisor de dos números; si uno es par y el otro impar, el programa debe hallar el mínimo común múltiplo
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
mcd = 1
i = 2
x = 1
y = 1
if a % 2 == 0 and b % 2 == 0 or a % 2 != 0 and b % 2 != 0:
    n = min(a,b)
    while i <= n:
       c = a / i 
       d = b / i
       c1 = int(c)
       d1 = int(d)
       if c-c1 == 0 and d-d1 == 0:
           mcd = mcd * i
           a = a / i
           b = b / i
           i = 1
       i = i + 1
    print(f"El máximo común divisor de ambos números es {mcd}")
else: 
    v1 = a
    v2 = b
    for z in range(1,(v1*v2)+1,+1):
        if z % v1 == 0 and z % v2 == 0: 
            print(f"{z} es el mínimo común múltiplo de {a} y {b}")
            break

    