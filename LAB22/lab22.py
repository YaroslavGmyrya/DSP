import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erfc

from itertools import batched

def Q(x):
    return 0.5 * erfc(x/np.sqrt(2))

def invert_table(table):
    return {v: k for k, v in table.items()}

def nearest_symbol(symbol, constellation):
    return min(constellation, key=lambda x: abs(symbol - x))

coeff1 = 1/np.sqrt(2)
coeff2 = 1/np.sqrt(10)

BPSK_mod_table = {
    "0": complex(-coeff1, -coeff1),
    "1": complex(coeff1, coeff1),
}

QPSK_mod_table = {
    "00": complex(-coeff1, -coeff1),
    "01": complex(-coeff1,  coeff1),
    "11": complex( coeff1,  coeff1),
    "10": complex( coeff1, -coeff1),
}

QAM16_mod_table = {
    "0000": complex(-3*coeff2, -3*coeff2),
    "0001": complex(-3*coeff2, -1*coeff2),
    "0011": complex(-3*coeff2,  1*coeff2),
    "0010": complex(-3*coeff2,  3*coeff2),

    "0100": complex(-1*coeff2, -3*coeff2),
    "0101": complex(-1*coeff2, -1*coeff2),
    "0111": complex(-1*coeff2,  1*coeff2),
    "0110": complex(-1*coeff2,  3*coeff2),

    "1100": complex( 1*coeff2, -3*coeff2),
    "1101": complex( 1*coeff2, -1*coeff2),
    "1111": complex( 1*coeff2,  1*coeff2),
    "1110": complex( 1*coeff2,  3*coeff2),

    "1000": complex( 3*coeff2, -3*coeff2),
    "1001": complex( 3*coeff2, -1*coeff2),
    "1011": complex( 3*coeff2,  1*coeff2),
    "1010": complex( 3*coeff2,  3*coeff2),
}

def BPSK_mod(bits):
    return [BPSK_mod_table[str(bit)] for bit in bits]

def QPSK_mod(bits):
    blocks = batched(bits, 2)
    return [QPSK_mod_table[''.join(map(str, block))] for block in blocks]

def QAM16_mod(bits):
    blocks = batched(bits, 4)
    return [QAM16_mod_table[''.join(map(str, block))] for block in blocks]

def QAM_mod(mod_type, bits):
    if mod_type == "BPSK":
        return BPSK_mod(bits)
    elif mod_type == "QPSK":
        return QPSK_mod(bits)
    elif mod_type == "QAM16":
        return QAM16_mod(bits)
    

BPSK_demod_table = invert_table(BPSK_mod_table)
QPSK_demod_table = invert_table(QPSK_mod_table)
QAM16_demod_table = invert_table(QAM16_mod_table)

def BPSK_demod(symbols):
    constellation = list(BPSK_demod_table.keys())
    bits = []

    for s in symbols:
        nearest = nearest_symbol(s, constellation)
        bits.append(BPSK_demod_table[nearest])

    return bits

def QPSK_demod(symbols):
    constellation = list(QPSK_demod_table.keys())
    bits = []

    for s in symbols:
        nearest = nearest_symbol(s, constellation)
        bits.append(QPSK_demod_table[nearest])

    return bits

def QAM16_demod(symbols):
    constellation = list(QAM16_demod_table.keys())
    bits = []

    for s in symbols:
        nearest = nearest_symbol(s, constellation)
        bits.append(QAM16_demod_table[nearest])

    return bits

def QAM_demod(mod_type, symbols):
    if mod_type == "BPSK":
        return BPSK_demod(symbols)
    elif mod_type == "QPSK":
        return QPSK_demod(symbols)
    elif mod_type == "QAM16":
        return QAM16_demod(symbols)
    
def AWGN(signal, snr_db):
    signal = np.asarray(signal)

    signal_power = np.mean(np.abs(signal)**2)

    snr_linear = 10**(snr_db / 10)

    noise_power = signal_power / snr_linear

    noise = (
        np.random.normal(0, np.sqrt(noise_power/2), signal.shape) +
        1j*np.random.normal(0, np.sqrt(noise_power/2), signal.shape)
    )

    return signal + noise

def equalize_zf(y, h):
    Y = np.fft.fft(y)
    H = np.fft.fft(h, n=len(y))

    X_hat = Y / H
    x_hat = np.fft.ifft(X_hat)

    return x_hat

GSM_TRANNING_SEQUENCE = np.asarray([0,1,0,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0])

h = [0.19 + 0.56j, 0.45 - 1.28j, -0.14 - 0.53j]
L = len(h)

# autocorr of traning sequence

# autocorrelation of full TRANING_SEQUENCE
autocorr_f = np.correlate(GSM_TRANNING_SEQUENCE, GSM_TRANNING_SEQUENCE, mode="full").astype(np.float64)
autocorr_f /= np.max(autocorr_f)

lags_f = np.arange(-len(autocorr_f)//2, len(autocorr_f)//2, 1)

# autocorrelation of 16 centering bits
slice_seq = GSM_TRANNING_SEQUENCE[4:len(GSM_TRANNING_SEQUENCE)-1]

autocorr_s = np.correlate(slice_seq, slice_seq, mode="full").astype(np.float64)
autocorr_s /= np.max(autocorr_s)

lags_s = np.arange(-len(autocorr_s)//2, len(autocorr_s)//2, 1)

# visualization
plt.plot(lags_f, autocorr_f, label="full autocorr")
plt.plot(lags_s, autocorr_s, label="slice autocorr")
plt.grid()
plt.legend()
plt.xlabel("lag")
plt.ylabel("R(lag)")
plt.title("Correlation comparing")
plt.show()



# generate data

N = 500
mod_type = "QPSK"
SNR = 20

# bits
bits = np.random.randint(0, 2, N)
bits = [*GSM_TRANNING_SEQUENCE, *bits] 

GSM_TRANNING_SEQUENCE = QAM_mod("QPSK", GSM_TRANNING_SEQUENCE)

# symbols
symbols = QAM_mod(mod_type, bits)

# multipath channel
rx_symbols = np.convolve(symbols, h)

# white noise
rx_symbols = AWGN(rx_symbols, SNR)

plt.scatter(np.real(rx_symbols), np.imag(rx_symbols))
plt.xlabel("I")
plt.ylabel("Q")
plt.title("RX Constellation")
plt.show()

# generate tranning sequence matrix
N = len(GSM_TRANNING_SEQUENCE)
T = np.zeros((N - L + 1, L), dtype=complex)

for i in range(L):
    T[:, L-1-i] = GSM_TRANNING_SEQUENCE[i:i + (N - L + 1)]

# extract tranning from 
y = rx_symbols[L-1:N]

# estimation
T_H = np.conjugate(T.T)

h_ls = np.linalg.inv(T_H @ T) @ T_H @ y

# compute MSE
mse = np.mean(np.abs((h - h_ls))**2)

print("MSE: ", mse)

x_hat = equalize_zf(rx_symbols, h)

x_hat = x_hat[len(GSM_TRANNING_SEQUENCE)-1:-2]

plt.scatter(np.real(x_hat), np.imag(x_hat))
plt.xlabel("I")
plt.ylabel("Q")
plt.title("RECOVERY SIGNAL")
plt.show()


rx_bits = QAM_demod(mod_type, x_hat)

print(rx_bits)