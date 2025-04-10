def quick(l):
    n = len(l)
    if n <= 1:
        return l
    else: 
        pivote = l[0]
    l1 = []
    l2 = []
    lp = [l[0]]
    for i in range (1, n):
        if l[i] < l[0]:
            l1.append(l[i])
        else: 
            l2.append(l[i])
    return quick(l1)+lp+quick(l2)
n = int(input("Ingrese el valor de datos a organizar: "))
x = []
for i in range(n):
    x.append(int(input(f"Ingrese el dato {i+1}: ")))
print("La lista es:", x)
print("La lista ordenada es:", quick(x))