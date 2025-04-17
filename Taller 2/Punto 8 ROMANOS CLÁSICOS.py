'''El programa se ejecuta mientras n sea diferente de 0, si n es igual a 0, el programa se acaba
el programa admite valores entre 0 y 4000. Ya que los números romanos clásicos llegan hasta 3999.
Lo que hice fue dividir n entre 10, para hallar las unidades, decenas, centenas y miles. 
Dependiendo de número de divisones se compara con los valores de abajo. Para hallar las 
unidades, decenas, centenas y miles, se utiliza la división % y // para que n se actualize
con un cociente entero'''
n = int(input("Ingrese el número a convertir: "))
while n != 0:
    if n > 0 and n < 4000:
        contador = 1
        final = ""
        for i in range(len(str(n))):
            l = n % 10
            n = n // 10
            if contador == 1:
                if l == 1:
                    final = "I" + final 
                elif l == 2:
                    final = "II" + final
                elif l == 3:
                    final = "III" + final 
                elif l == 4:
                    final = "IV" + final
                elif l == 5:
                    final = "V" + final  
                elif l == 6:
                    final = "VI" + final 
                elif l == 7:
                    final = "VII" + final 
                elif l == 8:
                    final = "VIII" + final 
                elif l == 9:
                    final = "IX" + final
            elif contador == 2:
                if l == 1:
                    final = "X" + final 
                elif l == 2:
                    final = "XX" + final
                elif l == 3:
                    final = "XXX" + final 
                elif l == 4:
                    final = "XL" + final
                elif l == 5:
                    final = "L" + final  
                elif l == 6:
                    final = "LX" + final 
                elif l == 7:
                    final = "LXX" + final 
                elif l == 8:
                    final = "LXXX" + final 
                elif l == 9:
                    final = "XC" + final
            elif contador == 3:
                if l == 1:
                    final = "C" + final 
                elif l == 2:
                    final = "CC" + final
                elif l == 3:
                    final = "CCC" + final 
                elif l == 4:
                    final = "CD" + final
                elif l == 5:
                    final = "D" + final  
                elif l == 6:
                    final = "DC" + final 
                elif l == 7:
                    final = "DCC" + final 
                elif l == 8:
                    final = "DCCC" + final 
                elif l == 9:
                    final = "CM" + final
            elif contador == 4:
                if l == 1:
                    final = "M" + final
                elif l == 2:
                    final = "MM" + final
                elif l == 3:
                    final = "MMM" + final
            contador += 1
        print(final)
    else:
        print("El número no cumple las condiciones")
    n = int(input("Ingrese el número a convertir: "))