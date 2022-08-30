import scipy
import numpy as np

def u(n):
    if n>=0:
        return 1
    else:
        return 0

def h(n):
    return u(n) * (-0.5)**n + u(n-2) * (-0.5)**(n-2) 

s = scipy.vectorize(h, otypes=[float])
k = np.arange(100)
print(np.sum(s(k)))
