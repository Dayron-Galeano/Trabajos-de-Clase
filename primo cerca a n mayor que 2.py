num = int(input("Ingresa un número mayor a 2: "))
i = 2
div = 0
for n in range(2,num+1):
    while i < n:
        if n % i == 0:
            div = div + 1
        i = i + 1
if div == 0:
    print(n)





