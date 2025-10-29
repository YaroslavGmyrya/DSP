import matplotlib.pyplot as plt
import numpy as np

#define timeline params
start = -0.003
stop = 0.003
dt = 0.00001
#define timeline
timeline = np.arange(start, stop, dt)

#define signal
f = 2000
signal = np.cos(2*np.pi*f*timeline)

#define impulse response
T = 0.001
h = [np.exp(-t/T) for t in timeline]

#convolve signal and h
conv = np.convolve(signal, h, mode="full")

t_conv_start = timeline[0] * 2
t_conv_stop  = timeline[-1] * 2

conv_timeline = np.arange(t_conv_start, t_conv_stop, dt)

#visualization
plt.subplot(3, 1, 1)
plt.plot(timeline, signal)
plt.xlabel("t,s")
plt.ylabel("A, V")
plt.title("Signal")
plt.subplot(3, 1, 2)
plt.plot(timeline, h)
plt.xlabel("t,s")
plt.ylabel("A, V")
plt.title("Impulse response")
plt.subplot(3, 1, 3)
plt.plot(conv_timeline, conv)
plt.xlabel("t,s")
plt.ylabel("A, V")
plt.title("Conv signal and h")
plt.show()

dw = 0.01
w = np.arange(-3/T, 3/T, dw)

AmpResp = 1 / np.sqrt((1 + (w*T)**2))
PhaseResp = -np.arctan(w*T)

plt.subplot(2, 1, 1)
plt.plot(w, AmpResp)
plt.xlabel("w,Hz")
plt.ylabel("|H(iw)|")
plt.title("Amp-freq response")
plt.subplot(2, 1, 2)
plt.plot(w, PhaseResp)
plt.xlabel("w,Hz")
plt.ylabel("phi(w)")
plt.title("Phase-freq response")
plt.show()

ph = -1.9
amp = 0.45
f = 2000

out_signal = amp * np.cos(2*np.pi * f * timeline + ph)

plt.plot(timeline, out_signal)
plt.xlabel("t,s")
plt.ylabel("A, V")
plt.title("Output signal")
plt.show()