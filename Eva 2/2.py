'''Se pide el número de elementos'''
n = int(input("Escriba el números de elementos: "))
'''se crea una lista donde iran los elemnetos'''
lista = []
'''se hace una variable que cuente el numero de posiciones pares, la suma de los numeros de las posiciones pares, ceros y 
se crea una variable que lleve la sumatoria de los numeros  en posiciones impares '''
npares = 0
pares = 0
impares = 0
ceros = 0
'''el for agrega los elemnetos a la lsita, además va sumamdo los números en posiciones pares e impares, y lleva el conteo de ceros'''
for i in range (n):
    lista.append(int(input(f"Escriba el elemento númerico, de la posición {i+1}: ")))
    if i % 2 == 0:
        npares += 1
        pares += lista[i]
    else: 
        impares += lista[i]
for i in range (n):
    if lista[i] == 0:
        ceros += 1
print(lista)
'''si la lista solo contiene ceros NO se ejecuta la siguiente parte de codigo'''
if ceros != n:
    '''se imprime la sumatoria de los números impares y la media de los números en posiciones pares'''
    print(f"El promedio de los números en posiciones pares es: {pares/npares}")
    print(f"La sumatoria de los números en posiciones impares es: {impares}")
    '''se crea una lista donde iran los mismos elementos pero dividos por el minimo o maximo de la lista, dependiendo de la posición'''
    lista2 = []
    maximo = max(lista)
    minimo = min(lista)
    '''si el numero minimo es igual 0, coge el siguiente número, es decir el segundo menor, esto se hace organizando la lista, si este tambien es 0, se entra en un while
    que va ir elemento por elemento buscando un número diferente de 0'''
    if minimo == 0:
        orden = sorted(lista)
        minimo = orden[1]
        if minimo == 0:
            i = 1
            while minimo == 0 and i <= n-1:
                minimo = orden[i]
                i += 1
    '''para los elementos en posiciones pares se divide el elemento por el maximo elemento, y para los elementos en posiciones impares se divide entre el menor. luego se agrega a la lista 2'''
    for i in range (n):
        if i % 2 == 0:
            lista2.append(lista[i]/maximo)
        else: 
            lista2.append(lista[i]/minimo)
    print(lista2)