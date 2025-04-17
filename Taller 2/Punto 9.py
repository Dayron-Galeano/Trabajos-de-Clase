'''Se pide los números en cadena, para poderlos escribir en una sola linea, además luego se
se separarán con spli'''
entrada = str(input("Escriba los números: "))
objetivo = int(input("Escriba la suma objetivo: "))
numeros = entrada.split()
print(numeros)
'''Lo que pasa a continuación es que escojemos un elemento de la lista, ya convertido en número
y lo vamos a sumar con los siguientes, para ver si sumados el resultado es igual al objetivo.
En el segundo for se usa i+1 ya que nos importan solo imprimir la primera posibilidad de cada pareja
es decir solo (a,b) no (a,b) y (b,a).
Luego se evalua si ambos números están en x, si lo están no se agregan nuevamente. Esto
se hace para evitar repetir números'''
nn = len(numeros)
x = []
for i in range(nn):
    num = int(numeros[i])
    for k in range(i+1,nn):
        c = int(numeros[k])
        if num + c == objetivo and num not in x and c not in x:
            x.append(num)
            x.append(c)
            print(f"[{num},{c}]")    
