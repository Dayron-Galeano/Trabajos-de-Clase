#Escribir un programa que lea un entero positivo y escriba el mismo número conformado por las cifras del número leído más 1. Si al sumar uno a una cifra da 10 se debe poner 0
n = str(input("Ingrese un número entero positivo: "))
pot = len(n)
numero = int(n)
z = ""
for i in range(pot):
    if int(n[i]) + 1 != 10:
        c = str(int(n[i]) + 1)
        z = z + c
    else: 
        z = z + "0"
print(z)
    