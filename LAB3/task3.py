import numpy as np

#import my function
import fourier_function as ff

# simple signal with once component and start phase = 0

#define constants
PI = np.pi
N = 6

# simple signal with many component and start phase != 0

#define signal params
A = 2
f = 2
T = 1/f
Ts = 0.001
phi_1 = PI/3
phi_2 = -PI/2

#define time line
t = np.arange(0,2,Ts)

#define samples for simple signal 
signal = A * np.cos(2*PI*f*t + phi_1) + np.cos(2*PI*2*f*t + phi_2)

ff.ft(signal, A, f, t, T, Ts, N)

#######################