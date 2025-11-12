import matplotlib.pyplot as plt
import numpy as np
import math

# discrete and non-discrete signals
f = 2
T = 0.4

t = np.arange(0, 4, 0.01)
t_d = np.arange(0, 4+T, T)

signal = np.cos(2*np.pi*f*t)
signal_d = np.cos(2*np.pi*f*t_d)


# recovery signal from samples
recovery_signal = []

for m in range(len(t)):
    sum = 0
    for n in range(len(t_d)):
        sum += signal_d[n] * np.sinc(1/T*(t[m] - n*T))

    recovery_signal.append(sum)

plt.show()
    
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel("t,s")
plt.ylabel("S(t)")

plt.plot(t_d, signal_d)
plt.xlabel("t,s")
plt.ylabel("S(t)")
plt.grid()
plt.legend(['non-discrete','discrete'])
plt.title("cos(4pi*t)")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, recovery_signal)
plt.xlabel("t,s")
plt.ylabel("S(t)")
plt.title("recovery signal")
plt.grid()
plt.show()


recovery_signal = []
tmp = []
for m in range(len(t)):
    sum = 0
    for n in range(len(t_d)):
        tmp.append(signal_d[n] * np.sinc(1/T*(t[m] - n*T)))

    recovery_signal.append(np.sum(tmp))
    
plt.plot(range(len(tmp)), tmp)
plt.show()