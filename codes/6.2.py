import numpy as np
import matplotlib.pyplot as plt
import scipy

N = 20
def u(n):
    if n <0:
        return 0
    else :
        return 1
def x(n):
    if n < 0 or n >5 :
        return 0
    elif n < 4:
        return n+1
    else :
        return 6-n

def h(n):
    return (-1/2)**n*u(n) + (-1/2)**(n-2)*u(n-2)

def X(k,N):
    sum  = 0
    for i in range(N):
        sum += x(i)*(np.exp(-1j*2*np.pi*i*k/N))
    return sum

def H(k,N):
    sum  = 0
    for i in range(N):
        sum += h(i)*(np.exp(-1j*2*np.pi*i*k/N))
    return sum
def Y(k,N):
    return H(k,N)*X(k,N)

vec_Y =  scipy.vectorize(Y)
k = np.arange(N)

plt.stem(k,vec_Y(k,N))
plt.xlabel("k")
plt.ylabel("$Y(k)$")
plt.grid()
plt.savefig("./figs/6.2.png")

plt.show()