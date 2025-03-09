n = int(input("Escriba el número a convertir: "))
b = int(input("Escriba la base a la cual quiere convertir el numero: "))
if 2 <= b < 10:
    if b == 2:
        cociente = n // 2
        r = n % 2
        guar = str(r)
        while cociente >= 2:
            r = cociente % 2
            cociente = cociente // 2
            guar = str(r) + guar
        guar2 = str(cociente)
        print(guar2 + guar)
    elif b == 3:
        cociente = n // 3
        r = n % 3
        guar = str(r)
        while cociente >= 3:
            r = cociente % 3
            cociente = cociente // 3
            guar = str(r) + guar
        guar2 = str(cociente)
        print(guar2 + guar)
    elif b == 4:
        cociente = n // 4
        r = n % 4
        guar = str(r)
        while cociente >= 4:
            r = cociente % 4
            cociente = cociente // 4
            guar = str(r) + guar
        guar2 = str(cociente)
        print(guar2 + guar)
    elif b == 5:
        cociente = n // 5
        r = n % 5
        guar = str(r)
        while cociente >= 5:
            r = cociente % 5
            cociente = cociente // 5
            guar = str(r) + guar
        guar2 = str(cociente)
        print(guar2 + guar)
    elif b == 6:
        cociente = n // 6
        r = n % 6
        guar = str(r)
        while cociente >= 6:
            r = cociente % 6
            cociente = cociente // 6
            guar = str(r) + guar
        guar2 = str(cociente)
        print(guar2 + guar)
    elif b == 7:
        cociente = n // 7
        r = n % 7
        guar = str(r)
        while cociente >= 7:
            r = cociente % 7
            cociente = cociente // 7
            guar = str(r) + guar
        guar2 = str(cociente)
        print(guar2 + guar)
    elif b == 8:
        cociente = n // 8
        r = n % 8
        guar = str(r)
        while cociente >= 8:
            r = cociente % 8
            cociente = cociente // 8
            guar = str(r) + guar
        guar2 = str(cociente)
        print(guar2 + guar)
    elif b == 9:
        cociente = n // 9
        r = n % 9
        guar = str(r)
        while cociente >= 9:
            r = cociente % 9
            cociente = cociente // 9
            guar = str(r) + guar
        guar2 = str(cociente)
        print(guar2 + guar)

        
            
            

