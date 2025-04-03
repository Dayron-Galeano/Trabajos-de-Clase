import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

def bubble_sort(L):
    n = len(L)
    for i in range(n - 1):
        for j in range(n - i - 1):
        #operaciones += 1
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
            #intercambios += 1
        print(f"paso {i + 1}: {L}")
    return 0

def insertion(L):
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j - 1] > L[j]:
        #operaciones += 1
            L[j], L[j - 1] = L[j - 1], L[j]
        #intercambios += 1
            j -= 1
        i += 1
        print(f"paso {i + 1}: {L}")
    return 0

def selection(L):
    for i in range(len(L) - 1):
        min = i
        for j in range(i + 1, len(L)):
            if (L[min] > L[j]):
                min = j
        if min != i:
            L[min], L[i] = L[i], L[min]
    return 0

num_elements = np.arange(100, 10001, 100)
size = num_elements.size
print(size)
#print(num_elements)
t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)
t_quick_sort = np.zeros(size)

for i, n in enumerate(num_elements) :
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    bubble_sort(vector_ord)
    t_final = perf_counter_ns()
    t_bubble[i] = t_final - t_inicio

for i, n in enumerate(num_elements) :
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    insertion(vector_ord)
    t_final = perf_counter_ns()
    t_insertion[i] = t_final - t_inicio

for i, n in enumerate(num_elements) :
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    selection(vector_ord)
    t_final = perf_counter_ns()
    t_selection[i] = t_final - t_inicio

plt.plot(num_elements, t_bubble, "g-", num_elements, t_insertion, "b-", num_elements, t_selection, "r-")
plt.show()