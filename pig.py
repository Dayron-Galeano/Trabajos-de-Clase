p = str(input("Escriba la palabra a transformar: "))
pos = len(p)
salida = ""
pig = "out"
primer = p[0]
#elegí agregar out a las palabras 
if p[0] == "a" or p[0] == "e" or p[0] == "i" or p[0] == "o" or p[0] == "u":
    print(p+pig)
else:
    for i in range(1,pos):
        salida = salida + p[i]
    print(salida + p[0] + pig)