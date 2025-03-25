import random as rnd
import matplotlib.pyplot as plt
X = [] 
Y = [] 
n = 10
for i in range(n):
    X.append(rnd.randint(0, 10))

print(X)

sumaX = 0
for i in range(len(X)):
    sumaX += X[i]

sumaY = 0
for i in range(len(X)):
    Y.append(X[i])
    sumaY += Y[i]

sumaXY = 0
for i in range(len(X)):
    xy = (X[i]*Y[i])
    sumaXY += xy

sumaX2 = 0
for i in range(len(X)):
    sumaX += (X[i])**2

m = (sumaXY - (((sumaX)*(sumaY))/n))/(sumaX2-(((sumaX)**2)/n))
print(m)

b = (sumaY/n)-(m*(sumaX/n))
print(b)

plt.plot(X, Y, "g-", (m*X)+b, "b-")
plt.show()