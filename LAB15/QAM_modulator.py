import matplotlib.pyplot as plt
import numpy as np
import math

dt = 5000

time = np.linspace(0, 1, dt)

f = 50

#define subcarrier
sin = -np.sin(2*np.pi*f*time)
cos = np.cos(2*np.pi*f*time)

#plot subcarriers
plt.subplot(2, 1, 1)

plt.plot(time, cos)
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Carrier cos")


plt.subplot(2, 1, 2)

plt.plot(time, sin)
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Carrier sin")

plt.show()

#create QAM signal on single symbol
I = 3
Q = 1

RF_signal = I*cos + Q*sin

#QAM signal spectrum
plt.plot(time, RF_signal)
plt.xlabel("time, s")
plt.ylabel("RF(t)")
plt.title("Carrier sin")
plt.show()

plt.plot(np.fft.fftfreq(len(RF_signal), 1/dt), np.abs(np.fft.fft(RF_signal)))
plt.xlabel("f, Hz")
plt.ylabel("S(f)")
plt.title("Amplitude-frequency spectrum")
plt.show()

#Add noise

m = 0
sigma = 0.3
noise = np.random.normal(m, sigma, len(RF_signal))

rx_rf_signal = RF_signal + noise

plt.plot(time, rx_rf_signal)
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Rx signal")
plt.show()

# RX
sin = -np.sin(2*np.pi*f*time + np.pi/9)
cos = np.cos(2*np.pi*f*time + np.pi/12)

RX_I = 2*cos * rx_rf_signal
RX_Q = 2*sin * rx_rf_signal

# I and Q in time
plt.subplot(2, 1, 1)
plt.plot(time, RX_I)
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("In-phase branch")

plt.subplot(2, 1, 2)
plt.plot(time, RX_Q)
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Quadrature branch")

plt.show()

# I and Q in frequency
plt.subplot(3, 1, 1)
plt.plot(np.fft.fftfreq(len(RX_I), 1/dt), np.abs(np.fft.fft(RX_I)))
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("In-phase branch")

plt.subplot(3, 1, 2)
plt.plot(np.fft.fftfreq(len(RX_Q), 1/dt), np.abs(np.fft.fft(RX_Q)))
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Quadrature branch")

#FIR
f_c = 25
w_c = 2*np.pi * f_c / 100

n = np.linspace(-20, 20, dt)
h = (w_c/np.pi) * np.sinc((w_c/np.pi) * n)
h = h / np.sum(h)

plt.subplot(3, 1, 3)
plt.plot(n, h)
plt.xlabel("time, s")
plt.ylabel("h(t)")
plt.title("Filter impulse response")
plt.show()

filter_output_I = np.convolve(RX_I, h, mode="same")
filter_output_Q = np.convolve(RX_Q, h, mode="same")

# #filter output

plt.subplot(2, 1, 1)
plt.plot(time, filter_output_I)
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("filter output I")

plt.subplot(2, 1, 2)
plt.plot(time, filter_output_Q)
plt.xlabel("f, Hz")
plt.ylabel("S(f)")
plt.title("filter output Q")

plt.show()

#Filter output spectrum
plt.subplot(2, 1, 1)
plt.plot(np.fft.fftfreq(len(filter_output_I), 1/dt), np.abs(np.fft.fft(filter_output_I)))
plt.xlabel("f, Hz")
plt.ylabel("S(f)")
plt.title("filter output I spectrum")

plt.subplot(2, 1, 2)
plt.plot(np.fft.fftfreq(len(filter_output_Q), 1/dt), np.abs(np.fft.fft(filter_output_Q)))
plt.xlabel("f, Hz")
plt.ylabel("S(f)")
plt.title("filter output Q spectrum")

plt.show()
