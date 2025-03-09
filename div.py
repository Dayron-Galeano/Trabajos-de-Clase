n = int(input("Escriba el número limitante: "))
i = 2
for i in range(n+1):
     if i%2 == 0 or i%3 == 0 or i%5 == 0:
          if i != 0:
               print(i)