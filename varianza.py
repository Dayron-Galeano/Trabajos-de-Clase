import random as rnd
x = []
n = int(input("Ingrese el número de datos: "))
for i in range(n):
    x.append(rnd.randint(0, 10))
media = sum(x)/n
minimo = min(x)
maximo = max(x)
y = []
for i in range(n):
    y.append((x[i]-media)**2)
varianza = sum(y)/n
desviacion = varianza**(1/2)
print(f"Los datos son: {x}")
print(f"La media es {media}")
print(f"La varianza es {varianza}")
print(f"La desviación estandar es {desviacion}")
print(f"El rango es {maximo-minimo}")
