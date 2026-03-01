import matplotlib.pyplot as plt
import numpy as np
import math

N = 128 #bits count
T = 0.001 #symbol duration
ns = 64 #samples per symbol
Ts = T/ns #discretization step
Ns = ns * N #points count

spec_collection = []

#frequency axis
f = np.fft.fftshift(np.fft.fftfreq(Ns, d=Ts))
mask = (f >= -750) & (f <= 750)

for i in range(21):
    #generate bits and symbols
    bits = np.random.randint(0,2, N)
    symbols = np.repeat(bits, ns)

    #compute DFT
    Sf = np.fft.fft(symbols, Ns)
    Sf = np.fft.fftshift(Sf)    

    #spectrum
    Pf = (Sf * np.conj(Sf)) * Ts / Ns    
    
    spec_collection.append(Pf[mask])
    
mean_cols = [sum(col)/len(col) for col in zip(*spec_collection)]
print(mean_cols)


plt.plot(f[mask], np.abs(Pf[mask]))
plt.xlabel("f, Hz")
plt.ylabel("S(f)")
plt.title("")
plt.grid(True)
plt.show()       

