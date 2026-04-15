import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# task 1

print("task 1:")

s1 = 1
s2 = 0

z = 0.52

sigma = 0.04

w_z1 = np.exp(-(z - s1)**2/(2*sigma))
w_z2 = np.exp(-(z - s2)**2/(2*sigma))

result = s1 if w_z1 > w_z2 else s2

print("Переданный символ:", result)
print("\n\n\n")

# task 2
print("task 2:")

A = [0.25, 1, 2, 4]

N0 = 0.5 * 2e-2
BW = Rb = 100

sigma = N0 * BW

t = np.linspace(0, 1, 1000)
noise = np.random.normal(0, sigma, len(t))

for a in A:
    sq_signal = a * signal.square(2 * np.pi * Rb * t)
    r = sq_signal + noise
        
    sample = r[4]
            
    w1 = np.exp(-(sample-a)**2/(2*sigma))
    w2 = np.exp(-(sample-0)**2/(2*sigma))
    
    result = 1 if w1 > w2 else 0
    
    print(f"A = {a} \t Bit = {result}")

print("\n\n")

# task 3
print("task3")

s1 = 1
s2 = -1

bit = np.random.randint(0, 2, 1)
symb = 2*bit-1

sigma = 0
n = np.random.normal(0, sigma, 1)

r = symb + n

result = r > (s1 + s2)/2

print(f"tx_bit={bit} \t rx_bit={result}\n\n")

# task 4

s1 = 1
s2 = -1
N = 1000


bit = np.random.randint(0, 2, N)
symb = 2*bit-1

sigma = 1.3
n = np.random.normal(0, sigma, N)

r = symb + n

rx_bits = [1 if r[i] > (s1+s2)/2 else 0 for i in range(len(r))]

BER = [0 if rx_bits[i] == bit[i] else 1 for i in range(len(r))]
BER = np.sum(BER) / len(BER)

print(f"BER={BER}")

# task 5

s1s = np.arange(0.25, 10, 0.25)

total_BER = []

for s in s1s:
    s1 = s
    s2 = -s1
    
    N = 1000


    bits = np.random.randint(0, 2, N)
    symb = [s1 if bit==1 else s2 for bit in bits]

    sigma = 10
    n = np.random.normal(0, sigma, N)

    r = symb + n

    rx_bits = [1 if r[i] > (s1+s2)/2 else 0 for i in range(len(r))]

    BER = [0 if rx_bits[i] == bits[i] else 1 for i in range(len(r))]
    BER = np.sum(BER) / len(BER)
    
    total_BER.append(BER)

plt.plot(s1s, total_BER, "-o")
plt.xlabel("s1")
plt.ylabel("BER")
plt.title("BER(s1)")
plt.grid()
plt.show()