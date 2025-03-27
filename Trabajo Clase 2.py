import random as rnd
import matplotlib.pyplot as plt
X = [] 
Y = [] 
xy = []
xx =[]
y2 = []
n = 10000
for i in range(n):
    X.append(rnd.randint(12,24))
sx = sum(X)

for i in range(n):
    Y.append(rnd.randint(150, 190))
sy = sum(Y)

for i in range(n):
    xy.append((X[i]*Y[i]))
sxy = sum(xy)

for i in range(n):
    xx.append(X[i]**2)
sxx = sum(xx)

m = ((sxy-((sx*sy)/n))/(sxx-(((sx)**2)/n)))

b = ((sy/n)-(m*(sx/n)))

for i in range(n):
    y2.append((X[i]*m)+b)

plt.plot(X, Y, "g*", X, y2, "b-")
plt.show()