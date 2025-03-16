# Construir un programa que lea un número entero mayor que 2 y devuelva como resultado el número primo de valor más cercano, en este caso menor o igual, al número leído
n = int(input("Ingrese un número (mayor a 2): "))
i = 2
numero = n
div = 0
if n > 2:
    while numero > 2:
        while i < numero:
            if numero % i == 0:
                div = div + 1
            i = i + 1
        if div == 0:
            print(numero)
            break
        i = 2
        div = 0
        numero = numero - 1
else: 
    print(f"{n} no cumple con la condición")
#hice que i empiece desde 2 y llega al valor anterior de numero, para que no tome en cuenta a 1 ni a numero mismo, y si los divores son iguales a 0 significa que es primo