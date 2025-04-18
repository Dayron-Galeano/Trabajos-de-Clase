frase_de_entrada = str(input("Escriba la frase a cifrar o descifrar: "))
opcion = str(input("Escriba Des(Para descifrar) o Cif(Para cifrar): "))
'''Decidi definir cifrar y descifrar, sabiendo que cifrar es sumar a la posición de cada letra.
Bajo esa idea, descifrar es restar a la posición de cada letra'''
def cifrar(frase):
    ''''Utilicé split, es una herramienta que permite dividir una frase, uno elige "separador" que
    se va a utilizar, en este caso queda como separador el espacio'''
    palabras = frase.split()
    num_palabras = len(palabras)
    '''Luego leo cuantas palabras hay en la frase'''
    print("Las palabras son:", num_palabras)
    frase_final = ""
    '''Creé la variable frase_final, la cual funciona para ir guardando valores'''
    for i in range (num_palabras):
        '''Evaluo cada palabra'''
        pf1 = ""
        pf2 = ""
        palabra = palabras[i]
        letras = len(palabra)
        if (i+1) % 2 == 0:
            '''Le sumé a i un uno, ya que como len va desde 0 hasta n-1, entonces el uno
            permite que queden con los números "verdaderos".
            Despúes se revisa si es par o impar con % 2'''
            for k in range (letras):
                nueva_palabra = ""
                '''Nueva_palabra sirve para ir guardando la palabra.
                Utilice chr() y ord(), la primera sirve para convertir de numeros a texto
                y la segunda es lo contrario, ambas se basan en la tabla ASCII.
                Luego defini unos casos especificos para unas letras, ya que al sumar el salto 
                que se debe hacer, se salen del abecedario'''
                if palabra[k] == "Z":
                    nueva_palabra = nueva_palabra + "C"
                elif palabra[k] == "z":
                    nueva_palabra = nueva_palabra + "c"
                elif palabra[k] == "Y":
                    nueva_palabra = nueva_palabra + "B"
                elif palabra[k] == "y":
                    nueva_palabra = nueva_palabra + "b"
                elif palabra[k] == "X":
                    nueva_palabra = nueva_palabra + "A"
                elif palabra[k] == "x":
                    nueva_palabra = nueva_palabra + "a"
                elif palabra[k] == "L":
                    nueva_palabra = nueva_palabra + "Ñ"
                elif palabra[k] == "l":
                    nueva_palabra = nueva_palabra + "ñ"
                elif palabra[k] == "M":
                    nueva_palabra = nueva_palabra + "O"
                elif palabra[k] == "m":
                    nueva_palabra = nueva_palabra + "o"
                elif palabra[k] == "N":
                    nueva_palabra = nueva_palabra + "P"
                elif palabra[k] == "n":
                    nueva_palabra = nueva_palabra + "p"
                elif palabra[k] == "Ñ":
                    nueva_palabra = nueva_palabra + "Q"
                elif palabra[k] == "ñ":
                    nueva_palabra = nueva_palabra + "q"
                elif palabra[k] not in [",",".",";"]:
                    nl = ord(palabra[k])
                    nueva_palabra = nueva_palabra + chr(nl+3)
                else:
                    nueva_palabra = nueva_palabra + palabra[k]
                pf2 = pf2 + nueva_palabra
                '''En frase_final se guarda la palabra final del proceso hecho anteriormente
                más lo ya habia'''
            frase_final = frase_final + " " + pf2
        elif (i+1) % 2 != 0:
            '''Aquí hago lo mismo pero con las palabras en posiciones impares.
            Y agrego otro caso especifico ya que en las posiciones impares el salto es de 4'''
            for k in range (letras):
                nueva_palabra = ""
                if palabra[k] == "Z":
                    nueva_palabra = nueva_palabra + "D"
                elif palabra[k] == "z":
                    nueva_palabra = nueva_palabra + "d"
                elif palabra[k] == "Y":
                    nueva_palabra = nueva_palabra + "C"
                elif palabra[k] == "y":
                    nueva_palabra = nueva_palabra + "c"
                elif palabra[k] == "X":
                    nueva_palabra = nueva_palabra + "B"
                elif palabra[k] == "x":
                    nueva_palabra = nueva_palabra + "b"
                elif palabra[k] == "W":
                    nueva_palabra = nueva_palabra + "A"
                elif palabra[k] == "w":
                    nueva_palabra = nueva_palabra + "a"
                elif palabra[k] == "L":
                    nueva_palabra = nueva_palabra + "O"
                elif palabra[k] == "l":
                    nueva_palabra = nueva_palabra + "o"
                elif palabra[k] == "M":
                    nueva_palabra = nueva_palabra + "P"
                elif palabra[k] == "m":
                    nueva_palabra = nueva_palabra + "p"
                elif palabra[k] == "N":
                    nueva_palabra = nueva_palabra + "Q"
                elif palabra[k] == "n":
                    nueva_palabra = nueva_palabra + "q"
                elif palabra[k] == "Ñ":
                    nueva_palabra = nueva_palabra + "R"
                elif palabra[k] == "ñ":
                    nueva_palabra = nueva_palabra + "r"
                elif palabra[k] == "K":
                    nueva_palabra = nueva_palabra + "Ñ"
                elif palabra[k] == "k":
                    nueva_palabra = nueva_palabra + "ñ"
                elif palabra[k] not in [",",".",";"]:
                    nl = ord(palabra[k])
                    nueva_palabra = nueva_palabra + chr(nl+4)
                else:
                    nueva_palabra = nueva_palabra + palabra[k]
                pf1 = pf1 + nueva_palabra
            frase_final = frase_final + " " + pf1
            '''Luego se utiliza replace(), para reemplazar el espacio inicial que se generaba al 
            imprimir la frase. Replace sirve definiendo que vas a reemplazar y con que lo harás,
            luego defines cuantas veces lo quieres hacer'''
    print(frase_final.replace(" ","",1))
def descifrar(frase):
    '''Descifrar como se dijo, es lo mismo que cifrar pero restando en vez de sumar'''
    palabras = frase.split()
    num_palabras = len(palabras)
    print("Las palabras son:", num_palabras)
    frase_final = ""
    for i in range (num_palabras):
        pf1 = ""
        pf2 = ""
        palabra = palabras[i]
        letras = len(palabra)
        if (i+1) % 2 == 0:
            for k in range (letras):
                nueva_palabra = ""
                if palabra[k] == "C":
                    nueva_palabra = nueva_palabra + "Z"
                elif palabra[k] == "c":
                    nueva_palabra = nueva_palabra + "z"
                elif palabra[k] == "B":
                    nueva_palabra = nueva_palabra + "Y"
                elif palabra[k] == "b":
                    nueva_palabra = nueva_palabra + "y"
                elif palabra[k] == "A":
                    nueva_palabra = nueva_palabra + "X"
                elif palabra[k] == "a":
                    nueva_palabra = nueva_palabra + "x"
                elif palabra[k] == "Ñ":
                    nueva_palabra = nueva_palabra + "L"
                elif palabra[k] == "ñ":
                    nueva_palabra = nueva_palabra + "l"
                elif palabra[k] == "O":
                    nueva_palabra = nueva_palabra + "M"
                elif palabra[k] == "o":
                    nueva_palabra = nueva_palabra + "m"
                elif palabra[k] == "P":
                    nueva_palabra = nueva_palabra + "N"
                elif palabra[k] == "p":
                    nueva_palabra = nueva_palabra + "n"
                elif palabra[k] == "Q":
                    nueva_palabra = nueva_palabra + "Ñ"
                elif palabra[k] == "q":
                    nueva_palabra = nueva_palabra + "ñ"
                elif palabra[k] not in [",",".",";"]:
                    nl = ord(palabra[k])
                    nueva_palabra = nueva_palabra + chr(nl-3)
                else:
                    nueva_palabra = nueva_palabra + palabra[k]
                pf2 = pf2 + nueva_palabra
            frase_final = frase_final + " " + pf2
        elif (i+1) % 2 != 0:
            for k in range (letras):
                nueva_palabra = ""
                if palabra[k] == "A":
                    nueva_palabra = nueva_palabra + "W"
                elif palabra[k] == "a":
                    nueva_palabra = nueva_palabra + "w"
                elif palabra[k] == "B":
                    nueva_palabra = nueva_palabra + "X"
                elif palabra[k] == "b":
                    nueva_palabra = nueva_palabra + "x"
                elif palabra[k] == "C":
                    nueva_palabra = nueva_palabra + "Y"
                elif palabra[k] == "c":
                    nueva_palabra = nueva_palabra + "y"
                elif palabra[k] == "D":
                    nueva_palabra = nueva_palabra + "Z"
                elif palabra[k] == "d":
                    nueva_palabra = nueva_palabra + "z"
                elif palabra[k] == "R":
                    nueva_palabra = nueva_palabra + "Ñ"
                elif palabra[k] == "r":
                    nueva_palabra = nueva_palabra + "ñ"
                elif palabra[k] == "Q":
                    nueva_palabra = nueva_palabra + "N"
                elif palabra[k] == "q":
                    nueva_palabra = nueva_palabra + "n"
                elif palabra[k] == "P":
                    nueva_palabra = nueva_palabra + "M"
                elif palabra[k] == "p":
                    nueva_palabra = nueva_palabra + "m"
                elif palabra[k] == "O":
                    nueva_palabra = nueva_palabra + "L"
                elif palabra[k] == "o":
                    nueva_palabra = nueva_palabra + "l"
                elif palabra[k] == "Ñ":
                    nueva_palabra = nueva_palabra + "K"
                elif palabra[k] == "ñ":
                    nueva_palabra = nueva_palabra + "k"
                elif palabra[k] not in [",",".",";"]:
                    nl = ord(palabra[k])
                    nueva_palabra = nueva_palabra + chr(nl-4)
                else:
                    nueva_palabra = nueva_palabra + palabra[k]
                pf1 = pf1 + nueva_palabra
            frase_final = frase_final + " " + pf1
    print(frase_final.replace(" ","",1))
while opcion != "Des" and opcion != "Cif":
    '''Luego utilizo el while para que se repita solicitar la opción, si la misma está mal.'''
    opcion = str(input("Escriba Des(Para descifrar) o Cif(Para cifrar): "))
if opcion == "Des":
    descifrar(frase_de_entrada)
elif opcion == "Cif":
    cifrar(frase_de_entrada)
    '''Hice más casos para las letras, ya que con el otro programa no contaba a la ñ'''