import numpy as np
import math as m
nxn = int(input("Ingrese el número de n: "))
if nxn == 0 or nxn <= 0:
    print("El número n debe ser mayor a 0")
    while nxn == 0 or nxn <= 0:
        nxn = int(input("Ingrese el número de n: "))
matriz_principal = []
for i in range (nxn):
    fila = []
    componentes= str((input(f"Escriba los componentes de la fila {i+1}: ")))
    componentes= componentes.split()
    n_componentes = len(componentes)
    if n_componentes != nxn:
        while n_componentes != nxn:
            componentes= str((input(f"Escriba los componentes de la fila {i+1}: ")))
            componentes= componentes.split()
            n_componentes = len(componentes)
    for a in range(n_componentes):
        fila.append(float(componentes[a]))
    matriz_principal.append(fila)
copia_matriz = [fila[:] for fila in matriz_principal]

print("La matriz es:")
for o in range (nxn):
    print(matriz_principal[o])
    
if nxn == 1:
    print(f"El determinante es {matriz_principal[0][0]}")

else:
    determinante = 1.0    
    for k in range (nxn):
        pivote = k
        max_v = abs(copia_matriz[0][0])
        for i in range (k+1, nxn):
            if abs(copia_matriz[i][k]) > max_v:
                max_v = abs(copia_matriz[i][k])
                pivote = i
        if pivote != k:
            copia_matriz[pivote], copia_matriz[k] = copia_matriz[k], copia_matriz[pivote]
            determinante = determinante*(-1)
        if copia_matriz[k][k] == 0:
            determinante = 0
            break
        else:    
            for i in range(k + 1, nxn):
                factor = copia_matriz[i][k] / copia_matriz[k][k]
                for j in range(k, nxn):
                    copia_matriz[i][j] -= factor * copia_matriz[k][j]
    for h in range (nxn):
        determinante = determinante * copia_matriz[h][h]
    print (f"La determinante es: {determinante}")
print("Matriz resultante para hallar la determinante:")
for z in range (nxn):
    print(copia_matriz[z])

if determinante == 0:
    print("No tiene inversa")
else:
    matriz = np.array(matriz_principal)
    identidad = np.identity(nxn)
    matriz_v = np.hstack((matriz, identidad))

    
    def ReduccionGaussJordan(A):
        for i in range(filas):
            for j in range(filas):
                if i != j :
                    if A[j, i] != 0:
                        factor = (-1) * (A[i, i] / A[j, i])
                        filatemp = A[i, :] + (factor) * A[j, :]
                        A[j, :] = filatemp
            
        for i in range(filas):
            A[i, :] /= (A[i, i])
        return A
    filas = nxn
    cols = filas + 1

    matriz_r = ReduccionGaussJordan(matriz_v)
    final1_matriz, final2_matriz = np.hsplit(matriz_r,2)
    print("La matriz inversa es:")
    print(final2_matriz)
