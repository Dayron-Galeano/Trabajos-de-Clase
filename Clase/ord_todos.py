import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

opcion = str(input("Ingrese una opción (Op: Para obtener el # de operaciones) o (Tm: Para obtener el tiempo que tarda): " )) 

def bubble_sort(L):
    operaciones = 0
    n = len(L)
    for i in range(n - 1):
        for j in range(n - i - 1):
            operaciones += 1
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                operaciones += 1
        #print(f"paso {i + 1}: {L}")

    return L, operaciones

def insertion_sort(L):
    operaciones = 0
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            operaciones += 1
            L[j], L[j - 1] = L[j - 1], L[j]
            operaciones += 1
            j -= 1
        i += 1
        

    return L, operaciones

def selection(L):
    operaciones = 0
    for i in range(len(L) - 1):
        min = i
        for j in range(i + 1, len(L)):
            operaciones += 1
            if (L[min] > L[j]):
                min = j
                operaciones += 1
        if min != i:
            L[min], L[i] = L[i], L[min]
        #intercambios += 1
            operaciones += 1
    return L, operaciones

num_elements = np.arange(100, 1001, 100)
print(num_elements)
size = num_elements.size
print(size)
#print(num_elements)
t_bubble = np.zeros(size)
ops_bubble = np.zeros(size)
t_selection = np.zeros(size)
ops_selection = np.zeros(size)
t_insertion = np.zeros(size)
ops_insertion = np.zeros(size)
t_quick_sort = np.zeros(size)

for i, n in enumerate(num_elements) :
    vector = np.random.randint(0, 100, n, dtype=np.int16) # se crea el vector a ordenar
    # acá se hace una copia de ese vector, para preservar el vector con números aleatorios.
    vector_ord = vector.copy()
    # acá viene la estructura para tomar el tiempo
    t_inicio = perf_counter_ns()
    A, ops = bubble_sort(vector_ord) # se ejecuta el método burbuja con el vector copia
    t_final = perf_counter_ns()
    ops_bubble[i] = ops # se guarda el tiempo para n elementos, para crear una gráfica.
    t_bubble[i] = t_final - t_inicio
    print(f"Vector ordenado: \n{A}")
    vector_ord = vector.copy() # volvemos a copiar el vector aleatorio original sobre el vector copia para
    # que el siguiente método trabaje sobre los mismos datos
    print(f"Vector sin ordenar: \n{vector_ord}")
    t_inicio = perf_counter_ns()
    A, ops = insertion_sort(vector_ord)
    t_final = perf_counter_ns()
    ops_insertion[i] = ops
    t_insertion[i] = t_final - t_inicio
    print(A)
    vector_ord = vector.copy()
    t_inicio = perf_counter_ns()
    A, ops = selection(vector_ord)
    t_final = perf_counter_ns()
    ops_selection[i] = ops
    t_selection[i] = t_final - t_inicio

if opcion == "Tm":
    plt.plot(num_elements, t_bubble, "g-", num_elements, t_insertion, "b-", num_elements, t_selection, "r-")
    plt.show()
elif opcion == "Op":
    plt.plot(num_elements, ops_bubble, "g-", num_elements, ops_insertion, "b-", num_elements, ops_selection, "r-")
    plt.show()
else:
    print("La opción es incorrecta, vuelva a ejecutar")