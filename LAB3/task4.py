########## Fourier series ##########

import numpy as np
import matplotlib.pyplot as plt

#import my function
import fourier_function as ff

#define constants
PI = np.pi
N = 10       # count elements in Fourier series

###### task 4 #######

# rectangle signal

#define signal params
T = 2        
tau = 0.5       
Fs = 1000       
t_max = 16

#define time line
t = np.arange(0, t_max, 1/Fs)

#define samples for simple signal 
signal = ((t % T) < tau).astype(float)

#get amps and phases components in signal
(a, b) = ff.ft(signal, 1, 1/T, t, T, Fs, N)

print(signal)

comp_list = [2,4,10]

for n in comp_list:
    new_signal = 0

    slice_a = a[:n + 1]
    slice_b = b[:n + 1]

    for k in range(1, n):
        new_signal += a[k]*np.cos(1/T*(k+1)*t) + b[k]*np.sin(1/T*(k+1)*t) 

    plt.plot(t, new_signal, label=f"{n}")
    plt.legend()
    plt.show()

########################