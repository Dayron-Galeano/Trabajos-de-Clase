'''Hice un while para que pregunte los coeficientes y en cuantas partes se quiere dividir
el rango [0-1], hasta que el polinomio sea de grado 20'''
exponentes = 0
while exponentes < 19:
    '''Hice un arreglo a lo pedido, el usuario no necesiita ingresar el grado del polinomio, con 
    solo los coeficientes se halla el grado,ya que el grado de un polinomio es el número
    de coeficientes - 1'''
    entrada = str(input("Ingrese los coeficientes: "))
    div = int(input("Ingrese el número a dividir el rango [0,1]: "))
    '''El split lo utilizo para separar los coeficientes, la separación es por espacios, por 
    eso div es una cadena'''
    coe = entrada.split()
    print("Coeficientes:",coe)
    exponentes = len(coe)-1
    '''Hace el proceso si el grado del polinomio es menor a 20'''
    if exponentes < 20:
        print("Grado del polinomio:",exponentes)
        '''el aumento es la medida de crecimiento desde 0 hasta 1, sin contar al 1,
        por ejemplo si queremos dividir el rango de 0-1, entre 10, cada rectangulo tendrá una
        base de 0.1, pero empezamos hasta 0, y llegamos hasta 0.9 Ya que sabemos que
        la esquina del lado izquierdo superior es el resultado de la función con el valor del ancho
        . Ahí estarían los 10 rectangulos'''
        aumento = 1/div
        print("Aumento:",aumento)
        '''r, cain y x valen 0, ya que r va a servir para guardar el resultado de cada
        evalución del polinomio con cada x. Cain va a guardar la cantidad de terreno de Caín. 
        Y por ultimo x vale 0 ya que empieza en 0 y va hasta 1/div(div-1)'''
        r , cain , x = 0, 0 , 0 
        '''El while como dije va de 0 hasta 1 sin contar al 1'''
        while x < 1:
            r = 0
            for i  in range(len(coe)):
                '''Evalua el polinomio con cada valor de x'''
                r = (int(coe[i]))*((x)**(exponentes-i))+r
            if r > 1:
                '''Si el resultado del for anterior es mayor a 1, se reemplaza por 1.
                Y se multiplica 1 x base que es el aumento'''
                cain = cain + (1*aumento)
            elif r < 0:
                '''Si el resultado del for anterior es menor a 0, se reemplaza por 0'''
                cain = cain
            else:
                '''Se multiplica el resultado(la altura) x la base, que es el aumento
                Después se suma con lo que ya habia en cain, porque es una sumatoria'''
                cain = (r*aumento) + cain
            '''X aumenta con el valor de aumento'''
            x += aumento 
        '''En la página se dice que el terreno de Abel es el 1 - el terreno de cain'''
        abel = 1 - cain
        '''Luego se imprime el terreno que le corresponde a cada uno'''
        print("Terreno de Caín:",cain)
        print("Terreno de Abel:", abel)
        '''Si el valor de la diferencia entre los terrenos es menor a 0.001, se considera justo.
        Pero si alguno de los dos hermanos tiene una diferencia a favor, mayor a 0.001, el 
        programa imprimira el nombre de ese hermano'''
        if abs(abel-cain) < 0.001:
            print("Justo")
        else:
            if abel > cain:
                print("Abel")
            elif cain > abel:
                print ("Caín")
    else: 
        '''Si el grado es 20 o mayor, el programa solo informara que el polinomio excede lo
        permitido'''
        print("Grado del polinomio:",exponentes)
        print("El grado del polinomio excede lo permitido")
        break