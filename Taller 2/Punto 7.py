'''nxn es el número de filas/columnas. Le dí un valor inicial de 1 para que "arranque" el while'''
nxn = 1
'''el while sirve para que pregunte constantemente nxn, si el nxn anterior es mayor a 0 y menor a 
51'''
while nxn > 0 and nxn < 51:
    nxn = int(input("Ingrese el número de filas: "))
    '''esto hace que si nxn es 0, se salga del ciclo'''
    if nxn == 0:
        break
    '''Cree una lista que contendrá otras listas, las cuales son las filas o vectores renglón'''
    matriz = []
    '''el siguiente for hace que se pida los componentes de cada fila, se 
    corten los separadores(espacios), se agreguen esos valores en valor númerico a una lista nueva
    para cada i, luego esas listas se agregan a "matriz" si tienen el mismo número de valores
    que nxn'''
    for i in range (nxn):
        n1 = []
        n = str((input(f"Escriba los componentes de la fila {i+1}: ")))
        n = n.split()
        leno = len(n)
        if leno != nxn:
            while leno != nxn:
                n = str((input(f"Escriba los componentes de la fila {i+1}: ")))
                n = n.split()
                leno = len(n)
        for a in range(leno):
            n1.append(int(n[a]))
        matriz.append(n1)
    '''Imprime cada fila, para que el usuario sepa'''
    for k in range(len(matriz)):
        print(matriz[k])   
    '''Hago un contador de no's. Primero evaluo la parte izquierda de la matriz, sumando
    todos los componentes desde 0 hasta nxn. Es decir en la lista 1, la suma dará el valor del
    componente en la posición 0, en  la lista 2, la suma dará = lista2[0] + lista2[1], y así 
    susecivamente, si el resultado es igual al componente que pertenece a la diagonal de esa
    lista, no se agregará un no. De lo contrario si se agrega, y se evaluá ahora la parte derecha
    de la matriz, del mismo modo que antes, pero ahora la suma va desde el componente perteneciente
    a la diagonal hasta el ultimo componente de la fila. Sí la matriz cumple que es triangular
    en la izquierda, no se ejecuta la evaluciación en la derecha de esta.
    Sí la matriz es triangular, el programa imprime "Sí", de lo contrario imprime "No"'''
    no = 0
    for z in range(len(matriz)):
        suma = 0
        helpa = matriz[z]
        for i in range(z+1):
            suma = suma + helpa[i]
        if suma != helpa[i]:
            no += 1
    if no > 0:
        no = 0
        for z in range(len(matriz)):
            suma = 0
            helpa = matriz[z]
            for i in range(nxn-1,z-1,-1):
                suma = suma + helpa[i]
            if suma != helpa[i]:
                no += 1
        if no > 0:
            print("No")
        else: 
            print("Sí")
    else: 
        print("Sí")
