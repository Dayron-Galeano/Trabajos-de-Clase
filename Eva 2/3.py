'''Se le pide al usuario la frase a convertir '''
frase = str(input("Escriba la frase: "))
'''Se corta la frase, utilizando como separador los espacios, para crear una lista que contega las palabras'''
palabras = frase.split()
'''Luego se crea la función, en la cual se define una cadena vacia que es "salida", con el for se va agregando cada palabra convertida a la cadena acompañada de un espacio. 
La palabra convertida se halla cogiendo la primera letra de la palabra y convirtiendola en mayuscula con .uppper y luego agregando el resto de palabra sin cambiar.'''
def mayuscula (palabras):
    salida = ""
    for i in range (len(palabras)):
        n = len(palabras[i])
        palabra = palabras[i][0].upper() + palabras[i][1:n]
        salida = salida + " " + palabra
    '''Luego como "salida" queda con un espacio inicial, lo que hago es cortar ese espacio con split, y utilizo 1, ya que esto significa que corta solo el primer espacio que encuentre'''
    texto = salida.split(" ",1)
    print(texto[1])
'''Se utiliza la función'''
mayuscula(palabras)