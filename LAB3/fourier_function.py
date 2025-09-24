import numpy as np
import matplotlib.pyplot as plt

#define constants
PI = np.pi

#define function to compute Fourier series
def ft(signal_samples, A, f, t, T, Ts, N):
    amps = []
    phases = []
    a =[]
    b = []
    for n in range(1,N + 1):
     
        #define subcarrier
        sc = A * np.cos(2*PI*f*t*n)
        ss = A * np.sin(2*PI*f*t*n)

        #compute signal and subcarrier mul
        mul_sc = signal_samples * sc
        mul_ss = signal_samples * ss

        #show original signal and subcarriers
        plt.subplot(N, 1, n)
        plt.plot(t, signal_samples, label="original signal")
        plt.plot(t, sc, label="np.cos component")
        plt.plot(t, ss, label="np.sin component")
        plt.xlabel('t, s')     
        plt.ylabel('A, B')  
        plt.title(f"Original signal and components, n = ${n}")
        plt.grid(True)
        plt.legend()  
    

        #compute coefficient of Fourier series (integration, dt = Ts)
        a_n = 2/T * np.sum(mul_sc) * Ts
        b_n = 2/T * np.sum(mul_ss) * Ts

        a.append(a_n)
        b.append(b_n)

        amps.append(np.sqrt(a_n ** 2 + b_n ** 2))
        if amps[-1] > 3:
            phases.append(np.arctan2(-b_n, a_n))

    plt.show()
    
    #show amplitude spectrum
    amp_ax = [n*f for n in range(1, N+1)]
    plt.subplot(1, 2, 1)
    plt.bar(amp_ax, amps, width=0.025)
    plt.xlabel("f, Hz")
    plt.ylabel("A, B")
    plt.title("Amplitude-frequnce spectrum")
    plt.grid(True) 

    #show phase spectrum
    if len(phases) > 1:
        plt.subplot(1, 2, 2)
        phase_ax = amp_ax[:len(phases)]
        plt.bar(phase_ax, phases, width=0.025)
        plt.xlabel("f, Hz")
        plt.ylabel("Phi, rad")
        plt.grid(True) 
        plt.title("Phase-frequnce spectrum")
    else:
        plt.subplot(1, 2, 2)
        plt.bar(0, 0, width=0.025)
        plt.xlabel("f, Hz")
        plt.ylabel("Phi, rad")
        plt.grid(True) 
        plt.title("Phase-frequnce spectrum")

    plt.show()

    return a, b
