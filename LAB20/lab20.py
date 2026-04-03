import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

b_count = 1000
oversamp = 4
Ts = 1/oversamp
SNR = 4

# generate data
bits = np.random.randint(0, 2, b_count)
bpsk_symb = 2*bits - 1

# oversampling
over_symb = np.repeat(bpsk_symb, oversamp)

plt.subplot(3, 1, 1)
plt.plot(over_symb)
plt.xlabel("sample")
plt.ylabel("A, V")
plt.title("oversampling symbols")

# calc energy on symbol
E_b = np.sum([over_symb[i]**2 for i in range(oversamp)]) * Ts

# calc noise lvl
SNR_lin = 10**(SNR/10)
sigma = np.sqrt(E_b/SNR_lin)

# generate noise
n = np.random.normal(0, sigma, len(over_symb))

# add noise
rx_signal = over_symb + n

plt.subplot(3, 1, 2)
plt.plot(rx_signal)
plt.xlabel("sample")
plt.ylabel("A, V")
plt.title("Rx symbols")

# MF filter
h = np.ones(oversamp)
mf = np.convolve(rx_signal, h, mode="full")

plt.subplot(3, 1, 3)
plt.plot(mf)
plt.xlabel("sample")
plt.ylabel("A, V")
plt.title("MF filter output")
plt.show()

# take samples in moment, when the symbol end
mf_samples = mf[oversamp-1::oversamp]

rx_bits = [1 if sample > 0 else 0 for sample in mf_samples]

BER = [0 if rx_bits[i] == bits[i] else 1 for i in range(len(bits))]
BER = np.sum(BER) / len(BER)

print(BER)