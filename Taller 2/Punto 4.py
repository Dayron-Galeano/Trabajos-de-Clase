casos = int(input("Número de casos a procesar: "))
for i in  range (casos):
    numero = int(input("Número: "))
    if numero > 0 and numero < 2**31 and int(numero**0.5) - numero**0.5 != 0:
        k = 1
        while int((numero*k)**0.5) - (numero*k)**0.5 != 0:
            k += 1
            resultadom = str(numero*k)
        print(f"La raíz es: {resultadom}**0.5", "Y el número es:", k)