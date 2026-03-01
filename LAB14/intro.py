import matplotlib.pyplot as plt
import numpy as np
import math

dt = 1/50000
tau = 0.05
t = np.arange(-tau/2, tau/2, dt)

signal = np.ones(len(t))

f_c = 100
carrier = np.cos(2*np.pi*f_c*t)

rf = signal * carrier

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.grid()
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Baseband")

plt.subplot(2, 1, 2)
plt.plot(t, carrier)
plt.grid()
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Carrier")

plt.show()

f_set = np.linspace(0, f_c*2, 6500)

ft_result = []

for f in f_set:
    e = np.exp(-1j * 2*np.pi*f * t)
    ft_result.append(np.sum(rf * e) * dt)

plt.subplot(3, 1, 1)
plt.plot(t, rf)
plt.grid()
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Radio signal")

plt.subplot(3, 1, 2)
plt.plot(f_set, np.abs(ft_result))
plt.grid()
plt.xlabel("f, Hz")
plt.ylabel("|S(f)|")
plt.title("Amplitude-frequency spectrum")

plt.subplot(3, 1, 3)
plt.plot(f_set, np.angle(ft_result))
plt.grid()
plt.xlabel("f, Hz")
plt.ylabel("|phi(f)|")
plt.title("Phase-frequency spectrum")
plt.show()
