n = int(input("Escriba el nùmero (entero positivo):"))
p = int(n)
# funciona para que en la resta del if se evidencie que es un entero, ya n - p = n - n = 0
opcion = str(input("Escriba la operaciòn que desea efectuar (Imp: Saber si el nùmero es impar o par) o (Prim: Saber si el nùmero es primo o no): "))
# elegì Imp y Prim como nombres para efectuar la operaciòn
if n >= 0 and n - p == 0:
    if opcion == "Imp":
        #evalua si la opciòn escrita es igual a Imp
        z = n % 2
        if z == 0:
        # si la divisòn de n entre 2 da como residuo 0, significa que es par, si sì deja residuo significa que es impar
            print(f"{n} es par")
        else:
            print(f"{n} es impar")
    elif opcion == "Prim":
        #evalua si la opciòn escrita es igual a Prim
        div = 0
        for i in range (1,n+1):
            z = n % i 
        # se evalua todos los divisores enteros de 1 hasta n, si solo hay 2 divisores se sabe que es primo
            if z == 0:
                div = div + 1
        if div == 2:
            print(f"{n} es primo")
        else: 
            print(f"{n} no es primo")
    else: 
        print("La opciòn no es correcta")

else:
    print("El nùmero no cumple las condiciones")
    