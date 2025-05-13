filas = int(input("Ingrese el número de filas:"))
colns = int(input("Ingrese el número de columnas:"))
matriz = []
if filas == 0 or filas <= 0 :
    print("El número de filas debe ser mayor a 0")
    while filas == 0 or filas <= 0:
        filas = int(input("Ingrese el número de filas: "))
if colns == 0 or colns <= 0:
    print("El número de columnas debe ser mayor a 0")
    while colns == 0 or colns <= 0:
        colns = int(input("Ingrese el número de columnas: "))
for i in range (filas):
    fila = []
    componentes= str((input(f"Escriba los componentes de la fila {i+1}: ")))
    componentes= componentes.split()
    n_componentes = len(componentes)
    if n_componentes != colns:
        while n_componentes != colns:
            componentes= str((input(f"Escriba los componentes de la fila {i+1}: ")))
            componentes= componentes.split()
            n_componentes = len(componentes)
    for a in range(n_componentes):
        fila.append(float(componentes[a]))
    matriz.append(fila)
for z in range (filas):
    print(matriz[z])
trasnpuesta = []
for a in range (colns):
    fila = []
    for b in range (filas):
        fila.append(matriz[b][a])
    trasnpuesta.append(fila)
for x in range (colns):
    print(trasnpuesta[x])
