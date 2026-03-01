import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import freqz, firwin
import math

# params
A = 53
f_pass = 2000
f_stop = 1500
fc = (f_pass + f_stop) / 2
fs = 30000
df = (f_pass - f_stop) / fs

# compute IR
norm_fc = (2*np.pi*fc)/fs 

N = math.floor(3.3/df)
M = N // 2

IR_axis = np.arange(-M, M)
shifted_IR_axis = np.arange(0, 2*M)

h = [(np.pi-norm_fc)/np.pi if n == 0 else -np.sin(norm_fc*n)/(np.pi*n) for n in IR_axis]

# show IR
plt.subplot(2, 1, 1)
plt.plot(IR_axis, h)
plt.xlabel("n")
plt.ylabel("h(n)")
plt.title("impulse response")
plt.subplot(2, 1, 2)
plt.plot(shifted_IR_axis, h)
plt.xlabel("n")
plt.ylabel("h(n)")
plt.title("Shifted impulse response")

plt.show()

# compute FR

H = np.fft.fftshift(np.fft.fft(h))
freq_hz_axis = np.fft.fftshift(np.fft.fftfreq(len(h), 1/fs))
freq_rad_axis = 2 * np.pi * freq_hz_axis / fs

#show FR in hz
plt.subplot(2,1,1)
plt.plot(freq_hz_axis, 20*np.log10(np.abs(H)))

# vertical line fc
plt.axhline(20*np.log10(-fc), label='f_c', color='blue')

# vertical line fp
# plt.axvline(fp, label='f_p', color='red')
# plt.axvline(-fp, color='red')
# plt.legend()

plt.xlabel("f, Hz")
plt.ylabel("|H(n)|db")
plt.title("Amplitude-frequence spectrum")

plt.subplot(2,1,2)
plt.plot(freq_hz_axis, np.angle(H))
plt.xlabel("f, Hz")
plt.ylabel("phi(f)")
plt.title("Phase-frequence spectrum")

plt.grid(True)

plt.show()

#show FR in rad/sample
plt.subplot(2,1,1)
plt.plot(freq_rad_axis, np.abs(H))

# plt.axvline(fc/fs*2*np.pi, label='f_c', color='blue')
# plt.axvline(-fc/fs*2*np.pi, color='blue')

# plt.axvline((fp)/fs*2*np.pi, color='red')
# plt.axvline((-fp)/fs*2*np.pi, label='f_p', color='red')
# plt.legend()


plt.xlabel("digital freq, rad/sample")
plt.ylabel("|H(n)|")
plt.title("Amplitude-frequence spectrum")

plt.subplot(2,1,2)
plt.plot(freq_rad_axis, np.angle(H))
plt.xlabel("digital freq, rad/sample")
plt.ylabel("phi(omega)")
plt.title("Phase-frequence spectrum")

plt.grid(True)

plt.show()


# generate signal with two component: f1 - in passband, f2 - in non-passband

f1 = 4000
f2 = 1200
Ts = 1/fs
t = np.arange(0, 0.3, Ts)

signal = np.cos(2*np.pi*f1*t) + np.cos(2*np.pi*f2*t)

plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Signal in time area")

plt.subplot(2, 1, 2)
plt.plot(np.fft.fftshift(np.fft.fftfreq(len(signal), Ts)), np.abs(np.fft.fftshift(np.fft.fft(signal))))
plt.xlabel("f, Hz")
plt.ylabel("S(f)")
plt.title("Signal in frequence area")
plt.show()

# convolve signal and IR
post_filter = np.convolve(signal, h, mode="same")

plt.subplot(2, 1, 1)
plt.plot(t, post_filter)
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Signal in time area")

plt.subplot(2, 1, 2)
plt.plot(np.fft.fftshift(np.fft.fftfreq(len(signal), Ts)), np.abs(np.fft.fftshift(np.fft.fft(post_filter))))
plt.xlabel("f, Hz")
plt.ylabel("S(f)")
plt.title("Signal in frequence area")
plt.show()

# create window

Nw = len(h)
hamming_window = 0.54 - 0.46 * np.cos(2*np.pi*np.arange(Nw)/(Nw-1))
#hamming_window /= np.sum(hamming_window)
plt.subplot(2, 1, 1)
plt.plot(shifted_IR_axis, hamming_window, label="window")
plt.plot(shifted_IR_axis, h, label="IR")
plt.legend()
plt.grid()

h_window = [h[i] * hamming_window[i] for i in shifted_IR_axis]

plt.subplot(2, 1, 2)
plt.plot(shifted_IR_axis, h_window)
plt.xlabel("n")
plt.ylabel("h(n)")
plt.ylabel("IR*window")
plt.show()

# build IR phase spectrum

new_H = np.fft.fftshift(np.fft.fft(h_window))
freq_hz_axis = np.fft.fftshift(np.fft.fftfreq(len(h_window), 1/fs))
freq_rad_axis = 2 * np.pi * freq_hz_axis / fs

#show FR in hz
plt.subplot(2,1,1)
plt.plot(freq_hz_axis, np.angle(H))
plt.xlabel("f, Hz")
plt.ylabel("phi(f)")
plt.title("Phase-frequence spectrum")

plt.subplot(2,1,2)
plt.plot(freq_hz_axis, np.angle(new_H))
plt.xlabel("f, Hz")
plt.ylabel("phi(f)")
plt.title("Phase-frequence spectrum")

plt.grid(True)

plt.show()

# convolve signal and new IR
post_filter = np.convolve(signal, h_window, mode="same")

plt.subplot(2, 1, 1)
plt.plot(t, post_filter)
plt.xlabel("time, s")
plt.ylabel("S(t)")
plt.title("Signal in time area")

plt.subplot(2, 1, 2)
plt.plot(np.fft.fftshift(np.fft.fftfreq(len(signal), Ts)), np.abs(np.fft.fftshift(np.fft.fft(post_filter))))
plt.xlabel("f, Hz")
plt.ylabel("S(f)")
plt.title("Signal in frequence area")
plt.show()