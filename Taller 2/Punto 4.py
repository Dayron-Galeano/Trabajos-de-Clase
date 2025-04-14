'''Se pregunta el número de casos y luego se pregunta para cada caso el número'''
casos = int(input("Número de casos a procesar: "))
for i in  range (casos): 
    numero = int(input("Número: "))
    '''Este if evalua si el número es mayor a 0 , menor a 2**31, y si el número no es un cuadrado
    perfecto. Ya que se me hace ilogico hacer el procedimiento, sabiendo que el número que va a dar
    es 1. Por ende, si el número escrito es un cuadrado perfecto, el programa no hára nada'''
    if numero > 0 and numero < 2**31 and int(numero**0.5) - numero**0.5 != 0:
        k = 1
        '''Acá se verifica si número*k no es un cuadrado perfecto, si llega a serlo, se
        acaba el while. Dando el menor número que multiplicado por "numero" de un cuadrado 
        perfecto'''
        while int((numero*k)**0.5) - (numero*k)**0.5 != 0:
            k += 1
            resultadom = str(numero*k)
        print(f"La raíz es: {resultadom}**0.5", "Y el número es:", k)
