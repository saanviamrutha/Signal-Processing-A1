import numpy as np
import matplotlib.pyplot as plt
from scipy import vectorize, linalg

def x(n):
    if n < 0 or n > 5:
        return 0
    elif n < 4:
        return n + 1
    else:
        return 6 - n

def u(n):
    if n >= 0:
        return 1
    else:
        return 0

def h(n):
    return u(n) * (-0.5)**n + u(n-2) * (-0.5)**(n-2) 

vec_x = vectorize(x, otypes=[float])
vec_h = vectorize(h, otypes=[float])

N = np.arange(20)
x_array = vec_x(N)
h_array = vec_h(N)

toeplitz_h = linalg.convolution_matrix(h_array, 20)
y_array = np.dot(toeplitz_h, x_array)

plt.stem(N, y_array[:20])
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.title('Filter Output using Convolution by Toeplitz Matrix')
#plt.savefig('../figs/5.9.png')
plt.show()