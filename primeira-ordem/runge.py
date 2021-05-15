import numpy as np
from matplotlib import pyplot as plt
import time
def f(x):
    return pow(x,2) + 2

def f2(x):
    return pow(x,3)/3 + 2*x + 1
x0 = 0
y0 = 1

xf = 10
h = 1

n = int((xf - x0)/h)

x = np.zeros(n + 1)
y = np.zeros(n + 1)

x[0] = x0
y[0] = y0

inicio = time.time()
for i in range(n):
    y[i + 1] = y[i] + f(x[i]) * h
    x[i + 1] = x[i] + h

fim = time.time()

print(fim-inicio)
y_exato = f2(x)

plt.plot(x, y_exato,label = 'Exato')
plt.plot(x,y, label = 'Método de Runge Kotta')
plt.title('método de runge - kutta de 1ª ordem')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('runge.png')
plt.show()