entrada = input("Frase a separar :")
con = " "
frase = entrada + con
n = len(frase)
salida = ""

for i in range(n):
    comp = frase[i] == con
    if comp != True:
        salida = salida + frase[i]
    else: 
        print(salida)
        salida = ""
   
   
        