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
    
N = 100
L = 4

SNR = 100
SNR_lin = 10**(SNR/10)

# generate bits
bits = np.random.randint(0, 2, N)

#generate symbols
BPSK_symbols = np.repeat(QAM_mod("BPSK", bits), L)
QPSK_symbols = np.repeat(QAM_mod("QPSK", bits), L)
QAM16_symbols = np.repeat(QAM_mod("QAM16", bits), L)


#add noise
ch_BPSK_symbols = AWGN(BPSK_symbols, SNR)
ch_QPSK_symbols = AWGN(QPSK_symbols, SNR)
ch_QAM16_symbols = AWGN(QAM16_symbols, SNR)

plt.subplot(3, 1, 1)
plt.scatter(np.real(ch_BPSK_symbols), np.imag(ch_BPSK_symbols))
plt.xlabel("I")
plt.ylabel("Q")
plt.title("Rx BPSK constellations")

plt.subplot(3, 1, 2)
plt.scatter(np.real(ch_QPSK_symbols), np.imag(ch_QPSK_symbols))
plt.xlabel("I")
plt.ylabel("Q")
plt.title("Rx QPSK constellations")

plt.subplot(3, 1, 3)
plt.scatter(np.real(ch_QAM16_symbols), np.imag(ch_QAM16_symbols))
plt.xlabel("I")
plt.ylabel("Q")
plt.title("Rx QAM16 constellations")

plt.show()


# matched filter

h = np.ones(L)

mf_BPSK_out = np.convolve(ch_BPSK_symbols, h)
mf_QPSK_out = np.convolve(ch_QPSK_symbols, h)
mf_QAM16_out = np.convolve(ch_QAM16_symbols, h)

plt.subplot(3, 1, 1)
plt.plot(np.real(mf_BPSK_out), label="REAL")
plt.plot(np.imag(mf_BPSK_out), label="IMAG")
plt.grid()
plt.legend()
plt.xlabel("I")
plt.ylabel("Q")
plt.title("MF BPSK output")

plt.subplot(3, 1, 2)
plt.plot(np.real(mf_QPSK_out), label="REAL")
plt.plot(np.imag(mf_QPSK_out), label="IMAG")
plt.grid()
plt.legend()
plt.xlabel("I")
plt.ylabel("Q")
plt.title("MF QPSK output")

plt.subplot(3, 1, 3)
plt.plot(np.real(mf_QAM16_out), label="REAL")
plt.plot(np.imag(mf_QAM16_out), label="IMAG")
plt.grid()
plt.legend()
plt.xlabel("I")
plt.ylabel("Q")
plt.title("MF QAM16 output")

plt.show()


#solver
rx_BPSK = mf_BPSK_out[L-1::L]
rx_QPSK = mf_QPSK_out[L-1::L]
rx_QAM16 = mf_QAM16_out[L-1::L]

rx_BPSK_bits = list(map(int, QAM_demod("BPSK", rx_BPSK)))
rx_QPSK_bits = list(map(int, QAM_demod("BPSK", rx_QPSK)))
rx_QAM16_bits = list(map(int, QAM_demod("BPSK", rx_QAM16)))

#BER
BPSK_BER = np.sum([1 if rx_BPSK_bits[i] != bits[i] else 0 for i in range(len(rx_BPSK_bits))])
BPSK_BER /= len(rx_BPSK_bits)

QPSK_BER = np.sum([1 if rx_QPSK_bits[i] != bits[i] else 0 for i in range(len(rx_QPSK_bits))])
QPSK_BER /= len(rx_QPSK_bits)

QAM16_BER = np.sum([1 if rx_QAM16_bits[i] != bits[i] else 0 for i in range(len(rx_QAM16_bits))])
QAM16_BER /= len(rx_QAM16_bits)

print(BPSK_BER)
print(QPSK_BER)
print(QAM16_BER)





