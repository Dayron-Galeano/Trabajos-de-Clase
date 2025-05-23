'''Se importa random ya que lo utilizare para crear las palabras de manera aleatoria'''
import random
'''Tambien math, para saber las posibles permutaciones, ya que la formula de estas son n!''' 
import math
palabra = str(input("Escriba la palabra: "))
'''Creo 2 listas, la primera para guardar las letras de la palabra dada por el usuario y que no 
estén repetidas.
La segunda lista es para guardar las permutaciones o palabras que se vayan generando'''
nueva = []
final = []
letras = len(palabra)
'''Definí la función aleatoridad, para que escoja una letra de las lista y luego la elimine, 
para que no se repita. Esta eliminación se hace mediante .pop. Y la selección aleatoria es 
mediante random'''
def aleatoriedad(a):
    aleatorio = random.randrange(len(a))
    letra = a.pop(aleatorio)
    return letra
'''El siguiente for hace que se revise si en la lista "nueva" no este el elemento palabra[i], para 
que no se repitan letras. Para eso se utiliza el not in'''
for i in range (letras):
    if palabra[i] not in nueva:
        nueva.append(palabra[i])
'''Se imprimen los elementos que se tienen en cuenta'''
print("Elementos que se tienen en cuenta:",nueva)
'''Se crea la variable n1 que sirve como guardado de nueva, para que luego nueva se la misma
que antes del while, ya que con el .pop, se irá
reduciendo'''
n1 = nueva
'''Utilizo factorial ya que eso me permite saber el número de posibles permutaciones,
y utilizo while, ya que como las palabras se forman aleatoriamente, existe la posibilidad de
que se repitan, si esto pasa, la lista no la tomara en cuenta, afectando el número de resultados'''
permutaciones = math.factorial(len(nueva))
while len(final) < permutaciones:
    pb = ""
    nueva = n1.copy()
    for z in range(len(nueva)):
        pb = pb + aleatoriedad(nueva)
    pbf = pb
    if pbf not in final:
        final.append(pbf)
'''Por ultimo imprimo cada palabra de final'''
for c in range(len(final)):
    print(f"La palabra número {c+1} es : {final[c]}")
