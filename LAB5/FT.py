import matplotlib.pyplot as plt
import numpy as np

# define rect signal param

# set time shift
t0 = 0

tau = 0.25
dt = 0.001
ofset = 0.1

# define rect signal

start = -tau/2 - ofset
end = tau/2 + ofset

timeline = np.arange(start,end,dt)

signal = [1 if i <= tau/2 + t0 and i >= -tau/2 + t0  else 0  for i in timeline]


plt.subplot(3, 1, 1)
plt.step(timeline, signal)
plt.xlabel("t,s")
plt.ylabel("A,v")
plt.title("Rectangle signal")
plt.grid()

# FT on [0, 3/tau]
N = 15
ft_result = []
f_ax = []

w_0 = 0

# uncomment if you want shift signal
#w_0 = 16 * 2 * np.pi

for i in range(0, N):
    
    w = i*1/(2 *tau) * 2 * np.pi
    
    f_ax.append(w / (2 * np.pi))
    
    e = np.exp(-1j * w * timeline)
    
    e_shift = np.exp(1j * w_0 * timeline)

    # S(t) * e^(-iwt)
    integral_func = signal * e * e_shift
    
    # numerical integration
    
    ft_result.append(np.sum(integral_func) * dt) 
    
    
plt.subplot(3, 1, 2)
plt.plot(f_ax, list(map(abs, ft_result)))
plt.xlabel("f,Hz")
plt.ylabel("A,v")
plt.title("Amplitude-frequence spectrum")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(f_ax, list(map(np.arctan2, [x.real for x in ft_result], [x.imag for x in ft_result])))
plt.xlabel("f,Hz")
plt.ylabel("Phaze,rad")
plt.title("Phase-frequence spectrum")
plt.grid()
plt.show()



