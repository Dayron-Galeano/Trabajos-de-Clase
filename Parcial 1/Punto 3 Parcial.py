n = str(input("Ingresa el número: "))
z = len(n)
print(f"{n} tiene {z} cifras")
# le dice al usuario cuantas cifras tiene el numero digitado
for i in range(z):
    op = int(n[i]) % 2 
    if op == 0:
        print(f" {int(n[i])} es par")
    else: 
        print(f" {int(n[i])} es impar")
# y luego se evalua para cada posiciòn si es par o impar dividiendo ese numero por 2, y mirando su residuo se define si es par o impar como se habia dicho
