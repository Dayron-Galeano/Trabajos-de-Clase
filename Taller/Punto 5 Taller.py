n = int(input("Escriba el número a convertir: "))
cociente = n // 2
r = n % 2
guar = str(r)
while cociente >= 2:
    r = cociente % 2
    cociente = cociente // 2
    guar = str(r) + guar
guar2 = str(cociente)
print("En base 2: ",guar2 + guar)
cociente = n // 4
r = n % 4
guar = str(r)
while cociente >= 4:
    r = cociente % 4
    cociente = cociente // 4
    guar = str(r) + guar
guar2 = str(cociente)
print("En base 4: ",guar2 + guar)
cociente = n // 8
r = n % 8
guar = str(r)
while cociente >= 8:
    r = cociente % 8
    cociente = cociente // 8
    guar = str(r) + guar
guar2 = str(cociente)
print("En base 8: ",guar2 + guar)
guar = ""
cociente = n
while cociente > 16:
    r = str(cociente % 16)
    if r == "10":
        r = "A"
    elif r == "11":
        r = "B"
    elif r == "12":
        r = "C"
    elif r == "13":
        r = "D"
    elif r == "14":
        r = "E"
    elif r == "15":
        r = "F"
    guar = r + guar
    cociente = cociente // 16
guar2 = str(cociente)
print("En base 16: ",guar2 + guar)