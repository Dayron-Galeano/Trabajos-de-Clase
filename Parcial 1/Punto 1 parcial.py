n = str(input("Ingrese el número a determinar si es capicúa: "))
#se utiliza que n sea cadena para poder invertirlo y evaluar si invertido, es el mismo número
print(f"El nùmero es {n}")
# se imprime n para saber que nùmero es (por si acaso)
z = len(n)
numero = ""
#numero es donde se ira guardando el nùmero invertido
for i in range(z):
    numero = str(n[i]) + numero
    print(numero)
    # se va imprimiendo el numero para ver como se va formando poco a poco
if numero == n:
    print("El nùmero es capicùa")
    # si el numero invertido es igual al que el usuario ingreso, es capicùa, de lo contrario, no lo es
else: 
    print("El nùmero no es capicùa")