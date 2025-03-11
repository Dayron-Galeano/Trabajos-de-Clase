n = int(input("Ingrese un número: "))
div = 0
if n > 2:
    for i in range(1,n+1):
        for z in range(1,i+1):
            if i % z == 0:
                div = div +1
    if div == 2:
        print(i)


