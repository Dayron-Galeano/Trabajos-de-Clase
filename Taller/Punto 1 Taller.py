#Construir un programa que lea un número variable de valores enteros. El resultado que entregara el programa es la media de los números pares de entre los leídos, es decir, la suma de todos los valores pares dividida por el número de estos. 
n = int(input("Ingrese el número de datos que va a poner: "))
i = 1
res = 0
np = 0
while i <= n:
    dato = int(input("Ingrese el valor: "))
    if dato % 2 == 0:
        res = res + dato
        np = np + 1
    i += 1
print(res/np)
#res es el acumulado a la suma de todos los pares, np es la cantidad de números pares, y por eso luego se imprime la división de res entre np