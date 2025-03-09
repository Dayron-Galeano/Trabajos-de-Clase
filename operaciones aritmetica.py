opcion = str(input("Escriba la operación que desea efectuar (Suma, Resta, Multiplicación, División), o si desea salir escriba (Salida):  "))
while opcion != "Salida":
    if opcion == "Suma":
        a = float(input("Escriba el primer termino: "))
        b = float(input("Escriba el segundo termino: "))
        print(a+b)
    elif opcion == "Resta":
        a = float(input("Escriba el primer termino: "))
        b = float(input("Escriba el segundo termino: "))
        print(a-b)
    elif opcion == "Multiplicación":
        a = float(input("Escriba el primer termino: "))
        b = float(input("Escriba el segundo termino: "))
        print(a*b)
    elif opcion == "División":
        a = float(input("Escriba el primer termino: "))
        b = float(input("Escriba el segundo termino: "))
        if b != 0:
            print(a/b)
    elif opcion == "Salida":
        opcion = "Salida"
    opcion = str(input("Escriba la operación que desea efectuar (Suma, Resta, Multiplicación, División), o si desea salir escriba (Salida):  "))

    
