entrada = input()
n = len(entrada)
i = 0
salida = ""
while i < n:
    if entrada[i] == "a":
        salida = salida + "A"
    elif entrada[i] == "e":
        salida = salida + "E"
    elif entrada[i] == "i":
        salida = salida + "I"
    elif entrada[i] == "o":
        salida = salida + "O"
    elif entrada[i] == "u":
        salida = salida + "U"
    else:
        salida = salida + entrada[i]
    i = i + 1
print(salida)
