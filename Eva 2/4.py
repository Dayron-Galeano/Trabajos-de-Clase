'''El usuario ingresa n, que como se ve es el número de elementos'''
n = int(input("Escriba el número de elementos:"))
'''Se crea una lista en la que con el for se irán agregando los elementos a esta'''
lista = []
for i in range (n):
    lista.append(int(i+1))
'''Se imprime la lista para que el usuario la vea, (por si acaso)'''
print(lista)
'''Se crea una segunda lista en la cual con el for, se irán agregando los elementos que estén en las posiciones de 3 en 3, empezando en 1, es decir en la lista2 estarán los elementos
de la "lista" con indice 1,4,7,10....'''
lista2 = []
for k in range(0,n,3):
    lista2.append(lista[k])
print(lista2)