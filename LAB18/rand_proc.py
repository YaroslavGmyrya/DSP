import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

m = 2
sigma = 4
N = 1000

X1 = np.random.normal(m, sigma, N)
X2 = np.random.uniform(0, 1, N)

t = np.linspace(0, 20, 1000)
sin = 4*np.sin(np.pi/3 * t)

plt.subplot(3, 1, 1)
plt.plot(X1)
plt.xlabel("n")
plt.ylabel("value")
plt.title("Normal signal")

plt.subplot(3, 1, 2)
plt.plot(X2)
plt.xlabel("n")
plt.ylabel("value")
plt.title("Uniform signal")

plt.subplot(3, 1, 3)
plt.plot(t, sin)
plt.xlabel("n")
plt.ylabel("value")
plt.title("Sin signal")

plt.show()

X1 = X1 + sin
X2 = X2 + sin

plt.subplot(2, 1, 1)
plt.plot(X1)
plt.xlabel("n")
plt.ylabel("value")
plt.title("Normal signal + sin")

plt.subplot(2, 1, 2)
plt.plot(X2)
plt.xlabel("n")
plt.ylabel("value")
plt.title("Uniform signal + signal")

plt.show()


plt.subplot(2, 1, 1)
plt.hist(X1, 350)
plt.xlabel("n")
plt.ylabel("value")
plt.title("Hist of normal signal + sin")

plt.subplot(2, 1, 2)
plt.hist(X2, 350)
plt.xlabel("n")
plt.ylabel("value")
plt.title("Hist of uniform signal + signal")

plt.show()


# calculate correlation

X1 -= np.mean(X1)

R_x1 = []

for k in range(len(X1)):
    summ = 0
    for n in range(len(X1) - k):
        summ += X1[n]*X1[n+k]
    
    R_x1.append(summ / (len(X1) - k))
    

X2 -= np.mean(X2)

R_x2 = []

for k in range(len(X2)):
    summ = 0
    for n in range(len(X2) - k):
        summ += X2[n]*X2[n+k]
    
    R_x2.append(summ / (len(X2) - k))
    
    
plt.subplot(2, 1, 1)
plt.plot(R_x1)
plt.xlabel("Shift")
plt.ylabel("B(shift)")
plt.title("X1 autocorr function")

plt.subplot(2, 1, 2)
plt.plot(R_x2)
plt.xlabel("Shift")
plt.ylabel("B(shift)")
plt.title("X2 autocorr function")

plt.show()


f1 = 4
f2 = 10

t = np.linspace(0, 1, 1000)
sin1 = 8*np.sin(2*np.pi * f1 * t)
sin2 = 8*np.sin(2*np.pi * f2 * t)

X1 = np.random.normal(0, 2, N)
X2 = np.random.normal(0, 2, N)

plt.subplot(2, 1, 1)
plt.plot(t, X1)
plt.xlabel("n")
plt.ylabel("value")
plt.title("Normal signal + sin")

plt.subplot(2, 1, 2)
plt.plot(t, X2)
plt.xlabel("n")
plt.ylabel("value")
plt.title("Uniform signal + signal")

plt.show()

numtaps = 31
f = 0.01

ir1 = signal.firwin(numtaps, f, pass_zero="highpass")
ir2 = signal.firwin(numtaps, f)


w, hw = signal.freqz(ir1, 1)

plt.subplot(2, 1, 1)
plt.stem(ir1)
plt.xlabel('Номер отсчета ИХ')
plt.ylabel('Отсчеты ИХ фильтра')

plt.subplot(2, 1, 2)
plt.stem(ir2)
plt.xlabel('Номер отсчета ИХ')
plt.ylabel('Отсчеты ИХ фильтра')

plt.show()

X1 = signal.lfilter(ir1, 1.0, X1)
X2 = signal.lfilter(ir2, 1.0, X2)

plt.subplot(2, 1, 1)
plt.plot(t, X1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("High speed component")

plt.subplot(2, 1, 2)
plt.plot(t, X2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Low speed component")
plt.show()


X1 -= np.mean(X1)

R_x1 = []

for k in range(len(X1)):
    summ = 0
    for n in range(len(X1) - k):
        summ += X1[n]*X1[n+k]
    
    R_x1.append(summ / (len(X1) - k))
    

X2 -= np.mean(X2)

R_x2 = []

for k in range(len(X2)):
    summ = 0
    for n in range(len(X2) - k):
        summ += X2[n]*X2[n+k]
    
    R_x2.append(summ / (len(X2) - k))
    
    
plt.subplot(2, 1, 1)
plt.plot(R_x1)
plt.xlabel("Shift")
plt.ylabel("B(shift)")
plt.title("X1 autocorr function")

plt.subplot(2, 1, 2)
plt.plot(R_x2)
plt.xlabel("Shift")
plt.ylabel("B(shift)")
plt.title("X2 autocorr function")

plt.show()
    
    


