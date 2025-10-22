import matplotlib.pyplot as plt
import numpy as np

def rect_signal(tau, t_shift, timeline, U):
    return [U if i <= tau + t_shift and i >= 0 + t_shift  else 0  for i in timeline]


start = -5
end = 5
dt = 0.01
timeline = np.arange(start,end,dt)

U = 4
signal = rect_signal(1, 0, timeline, U)
plt.subplot(2, 1, 1)
plt.step(timeline, signal)
plt.xlabel("t,s")
plt.ylabel("A,v")
plt.title("Rectangle signal")
plt.grid()

#define convolution params

T = 2

h = [1/T*np.exp(-t/T) for t in timeline]

plt.subplot(2, 1, 2)
plt.step(timeline, h)
plt.xlabel("t,s")
plt.ylabel("A,v")
plt.title("Impulse response")
plt.grid()

plt.show()

rect_shift = [-1, 0, 2]
plt_num = 1

#shifting rectangle signal
for shift in rect_shift:
    tmp_signal = rect_signal(1, shift, timeline, U)
    
    plt.subplot(len(rect_shift), 1, plt_num)
    plt.step(timeline, tmp_signal)
    plt.plot(timeline, h)
    plt.xlabel("t,s")
    plt.ylabel("A,v")
    plt.title(f"Shift rect signal, shift={shift}")
    plt.grid()
    plt_num += 1
    
plt.show()

#mul rect signal and h

for shift in rect_shift:
    tmp_signal = rect_signal(1, shift, timeline, U)
    mul_signal = [tmp_signal[i] * h[i] for i in range(len(timeline))]
    integral = np.sum(mul_signal)* dt
    print(f"shift = {shift} \t integral = {integral}")
    
# integration. shift = 0.2

shift = 0.2
tmp_signal = rect_signal(1, shift, timeline, U)
mul_signal = [tmp_signal[i] * h[i] for i in range(len(timeline))]
integral = np.sum(mul_signal)* dt

shifts = np.arange(-10, 10, dt)
integral = []

for shift in shifts:
    tmp_signal = rect_signal(1, shift, timeline, U)
    mul_signal = [tmp_signal[i] * h[i] for i in range(len(timeline))]
    integral.append(np.sum(mul_signal)* dt)

plt.plot(shifts, integral)
plt.ylabel("A, V")
plt.xlabel("t, s")
plt.title("Output signal")
plt.show()