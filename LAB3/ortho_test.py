import numpy as np

PI = np.pi

def ortho_test(k, n, F_s, f, t):
    for i in range(len(k)):
        #define signal
        signal_1 = np.sin(2*PI*f*t*k[i])
        signal_2 = np.sin(2*PI*f*t*n[i])

        #mul signal
        mul_signal = signal_1 * signal_2

        #discrete integration
        integral = np.sum(mul_signal) * 1/F_s

        print(f"k = {k[i]}, n = {n[i]} \t Integral = {integral}")