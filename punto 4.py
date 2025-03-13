a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
mcd = 1
i = 2
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
print(mcd)
        