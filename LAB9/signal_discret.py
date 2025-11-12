import matplotlib.pyplot as plt
import numpy as np
import math

#define params
H0 = 1

#f_c
fc = 200
wc = 2*np.pi * fc

#filter delay
t0 = 0.02

fs = 1/(10**4)
timeline = np.arange(0, 2*t0, fs)

#generate impulse response
impulse_response = 2*H0*fc * np.sinc(fc * (timeline - t0))

#buid plot
plt.plot(timeline, impulse_response)
plt.grid()
plt.xlabel("time")
plt.ylabel("h(t)")
plt.title("Импульсная характеристика ФНЧ")
plt.show()

#integration impulse response
f_range = np.arange(-5000,5000, 1)
w_range = f_range * 2 * np.pi

H = [np.sum(impulse_response*np.e**(-1j*w0*timeline)) * fs for w0 in w_range]

plt.subplot(2, 1, 1)
plt.plot(f_range, np.abs(H))
plt.xlabel("w,rad")
plt.ylabel("|H(iw|")
plt.title("АЧХ фильтра")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(f_range,  [-t0*x for x in w_range])
plt.xlabel("w,rad")
plt.ylabel("ф(w)")
plt.title("ФЧХ фильтра")
plt.grid()
plt.show()