import numpy as np
'''se pide el tamaño nxn'''
n = int(input("Escriba el tamaño n de la matriz: "))
'''se crea una matriz, con elementos random 0-99 de tamaño nxn, con las funciones de numpy'''
matriz_aleatoria = np.random.randint(low= 0, high= 100, size=(n, n))
print(matriz_aleatoria)
'''se crean las variables que guardaran las sumas de las diagonales, siendo suma1 la suma de la diagonal principal y suma2 siendo de la diagonal secundaria'''
suma1 = 0
suma2 = 0
for i in range (n):
    suma1 += matriz_aleatoria[i,i]
    '''se hallan los elementos de la diagonal secundaria, que por ejemplo para un 3x3. empieza con el elemento 13, luego 22 y por ultimo 31, entonces por eso suma 2 queda de esa manera'''
    suma2 += matriz_aleatoria[i,n-1-i]
'''para hallar el promedio de ambas, se dividen las 2 sumas entre el numeros de elementos de la diagonal que es el mismo que n'''
print(f"El promedio de la diagonal principal es: {suma1/n}")
print(f"El promedio de la diagonal secundaria es: {suma2/n}")
