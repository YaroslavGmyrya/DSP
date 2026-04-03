import matplotlib.pyplot as plt
import numpy as np
import math

def shift_array(arr, k):
    k = k % len(arr)  
    return arr[-k:] + arr[:-k] 

def corr(a, b):   
    return np.sum(a * np.conj(b))

def norm_corr(a, b):
    if len(a) != len(b):
        print("List must be have same len!")
        return
    
    norm_a = np.sum(np.abs(a)**2)
    norm_b = np.sum(np.abs(b)**2)

    return np.abs(corr(a,b) / (np.sqrt(norm_a) * np.sqrt(norm_b)))

# model parameters
bins = 500
points_count = 10000
M = 30
tau = 0

# example of uniform distr
t = np.linspace(0,3,points_count)
x_uf = np.random.uniform(0,1,points_count)

plt.hist(x_uf, bins)
plt.xlabel("Значение СВ")
plt.ylabel("Кол-во попаданий")
plt.title("Плотность распределения")
plt.show()

# sum of uniform distr
y = []
sum = np.zeros(points_count)
for i in range(M):
    y.append(np.random.uniform(0,1,points_count))
    sum += y[-1]

# hist
plt.hist(sum, bins)
plt.xlabel("Значение СВ")
plt.ylabel("Кол-во попаданий")
plt.title("Плотность распределения")
plt.show()

# autocorr
ACF = np.zeros(len(y[0]))
for i in range(len(y)):
    ACF += np.correlate(y[i]-np.mean(y[i]), y[i]-np.mean(y[i]), mode="same")
    
    
plt.plot(ACF[len(ACF)//2:] / len(y))
plt.title("ACF")
plt.xlabel("lags")
plt.ylabel("R")
plt.show()

# generate realization of normal distr
t=np.linspace(0,3,100)

norm_proc = []
proc_n = 100000

for i in range(proc_n):
    norm_proc.append(np.random.normal(0,5,len(t)))
    
# h - IR channel
h = [1,0.7, 0.3, 0.1, 0.05]

for i in range(len(norm_proc)):
    norm_proc[i] = np.convolve(norm_proc[i], h, mode="full")
    
index = np.sort(np.random.randint(0, len(norm_proc[0]), len(norm_proc)))


slices = []
for i in range(len(norm_proc)):
    slices.append(norm_proc[i][index[i]])
    
plt.subplot(3, 1, 1)
plt.plot(index, slices)

plt.subplot(3, 1, 2)
plt.hist(slices, 300)

plt.subplot(3, 1, 3)
plt.plot(np.correlate(norm_proc[0], norm_proc[0], mode="same"))

plt.show()


x = np.random.normal(0, 1, 1000)
x = x - np.mean(x)

max_tau = 100
R = []

for tau in range(max_tau + 1):
    R_tau = np.mean(x[:len(x)-tau] * x[tau:])
    R.append(R_tau)

R = np.array(R)
rho = R / R[0]

tau_corr = np.where(rho < 1/np.e)[0][0]
print("Correlation Interval", tau_corr)

plt.plot(range(max_tau + 1), rho)
plt.xlabel("tau")
plt.ylabel("ACF")
plt.grid(True)
plt.show()
