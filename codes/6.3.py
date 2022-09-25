import numpy as np
import matplotlib.pyplot as plt
import scipy
#If using termux
'''import subprocess
import shlex'''
#end if


N = 20
n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

def x(n):
    if n < 0 or n >5 :
        return 0
    elif n < 4:
        return n+1
    else :
        return 6-n


def y(n):
    if n < 0:
        return 0
    else:
        return x(n) + x(n-2) - 0.5 * y(n-1)

def u(n):
    if n <0:
        return 0
    else :
        return 1


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
def y_idft(n,N):
	sum = 0
	for i in range(N):
		sum+= Y(i,N)*np.exp((2j* np.pi *i*n)/N)
	return np.real(sum)/N


#print(X)

y_dif = scipy.vectorize(y)

k = np.arange(N)
#plots
plt.stem(k,y_idft(k,N),markerfmt='bo')

plt.stem(k,y_dif(k),linefmt = "r--",markerfmt = 'ro')
plt.title('Filter Output using DFT')
plt.legend(['IDFT','Difference'])
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
#
#If using termux
# plt.savefig('../figs/yndft.pdf')
# subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
#else
plt.savefig("./Figs/6.3.png")
plt.show()