import matplotlib.pyplot as plt
import numpy as np
import math

# functions
def my_dft(x, N):
    y = []
    for n in range(N):
        summ = 0
        for k in range(N):
            summ += x[k] * np.e ** ((-1j*2*np.pi*n*k)/N)
        y.append(summ/N)
    return y

def my_idft(x, N):
    y = []
    for n in range(N):
        summ = 0 + 0j
        for k in range(N):
            summ += x[k] * np.e ** ((1j*2*np.pi*n*k)/N)
        y.append(summ)
    return y

def my_fft_shift(x):
    N = len(x)
    
    left  = x[:N//2]    
    right = x[N//2:]     
    
    return right + left
  
#define signal
f = 32
f2 = 7

fs = 32 * f
Ts = 1/fs 

N = 16

t = np.arange(0, 2, Ts)
#signal = np.cos(2*np.pi*f*t) + np.cos(2*np.pi*f2*t)

signal = [0] * 16
signal[2] = 5+10j
signal[14] = 5-10j


recovery_signal = my_idft(signal, N)
time_axis = np.arange(0, N) / fs
plt.plot(time_axis, np.real(recovery_signal))
plt.xlabel("n,samples")
plt.ylabel("S[n]")
plt.title("Recovery signal")
plt.grid(True)
plt.show()

# plt.stem(t, signal)
# plt.xlabel("n,samples")
# plt.ylabel("S[t]")
# plt.title("Discrete signal")
# plt.grid(True)
# plt.show()

# #dft
# signal_fft = my_fft_shift(my_dft(signal, N))
# print(abs(signal_fft[56]))

# freq_step = fs/N

# f_ax = np.arange(-fs//2, fs//2, freq_step)

# plt.stem(f_ax, np.abs(signal_fft))
# plt.xlabel("f,Hz")
# plt.ylabel("S[iw]")
# plt.title("Amplitude-frequence spectrum")
# plt.grid(True)
# plt.show()


# recovery_signal = my_idft(signal_fft, N)
# time_axis = np.arange(0, N) / fs
# plt.stem(time_axis, np.real(recovery_signal))
# plt.xlabel("n,samples")
# plt.ylabel("S[n]")
# plt.title("Recovery signal")
# plt.grid(True)
# plt.show()