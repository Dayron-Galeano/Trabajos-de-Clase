frase_de_entrada = str(input("Escriba la frase a cifrar o descifrar: "))
opcion = str(input("Escriba Des(Para descifrar) o Cif(Para cifrar): "))
def cifrar(frase):
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
                elif palabra[k] not in [",",".",";"]:
                    nl = ord(palabra[k])
                    nueva_palabra = nueva_palabra + chr(nl+3)
                else:
                    nueva_palabra = nueva_palabra + palabra[k]
                pf2 = pf2 + nueva_palabra
            frase_final = frase_final + " " + pf2
        elif (i+1) % 2 != 0:
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
                elif palabra[k] not in [",",".",";"]:
                    nl = ord(palabra[k])
                    nueva_palabra = nueva_palabra + chr(nl+4)
                else:
                    nueva_palabra = nueva_palabra + palabra[k]
                pf1 = pf1 + nueva_palabra
            frase_final = frase_final + " " + pf1
    print(frase_final.replace(" ","",1))
def descifrar(frase):
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
                elif palabra[k] not in [",",".",";"]:
                    nl = ord(palabra[k])
                    nueva_palabra = nueva_palabra + chr(nl-4)
                else:
                    nueva_palabra = nueva_palabra + palabra[k]
                pf1 = pf1 + nueva_palabra
            frase_final = frase_final + " " + pf1
    print(frase_final.replace(" ","",1))
while opcion != "Des" and opcion != "Cif":
    opcion = str(input("Escriba Des(Para descifrar) o Cif(Para cifrar): "))
if opcion == "Des":
    descifrar(frase_de_entrada)
elif opcion == "Cif":
    cifrar(frase_de_entrada)