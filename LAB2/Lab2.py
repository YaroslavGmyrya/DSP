import numpy as np
import matplotlib.pyplot as plt

#define sub constant
PI = np.pi

#define signal params
A = [13, 30]
F = [3, 6]
PHI = [30, 270]

if(len(A) + len(F) + len(PHI) != len(A) * 3):
    print("Signal params must be same length")
    exit(1)

#define time params
LEFT = 0
RIGHT = 2000
STEP = 1

#define signals
def complex_signal_1(f, t):
    result  = []

    for i in range(len(t)):
        result.append(4/PI * np.cos(2 * PI * f * t[i] - PI/2) + 4/(3*PI) * np.cos(2 * PI * 3 * f * t[i] - PI/2))

    return result

def complex_signal_2(n, f, t):
    result  = []

    for i in range(len(t)):
        result.append(4 / ((2*n - 1) * PI) * np.cos(2 * PI * (2*n - 1) * f * t[i] - PI/2))

    return result

def base_signal(A, f, t, phi):
    result = []

    for i in range(len(t)):
        result.append(A * np.sin(2 * PI * f * t[i] + (phi * PI) / 180))

    return result

#init time ax
t = np.linspace(LEFT, STEP, RIGHT)

signals_vals_collection = []

#create and show 2 base signal with same frequences
plt.figure()
for i in range(len(F)):
    signals_vals_collection.append(base_signal(A[i], F[0], t, PHI[i]))
    plt.subplot(len(F) + 1, 1, i+1)
    plt.plot(t, signals_vals_collection[i])
    plt.title(f"{A[i]}sin(2*pi*{F[0]} + {PHI[i]})")


#sum 2 signal with same frequences
sum_list = []
for signal in zip(*signals_vals_collection):
    sum_list.append(np.sum(signal))

plt.subplot(len(F) + 1, 1, len(signals_vals_collection) + 1)
plt.plot(t, sum_list)
plt.title("Complex signal")
plt.show()

complex_signal = complex_signal_1(F[0], t)

plt.plot(t, complex_signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("Signal")
plt.show()

complex_signal_collection = []

F = [3, 6, 9, 12, 15, 18]
res_complex_signal = []

for n in range(len(F)):
    complex_signal_collection.append(complex_signal_2(n, F[i], t))


for signal in zip(*complex_signal_collection):
    res_complex_signal.append(np.sum(signal))


plt.plot(t, res_complex_signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("Signal")
plt.show()


######## SHOW COMPLEX EXP ########

# define time line
t = np.linspace(0, 2.5, 250)

# complex exp
f = np.exp(2 * np.pi * 2 * 1j * t)

# create figure
fig = plt.figure(figsize=(8,8))
ax = plt.axes(projection='3d')
ax.grid()

# get real and image components
x = f.real
y = f.imag

# main path
ax.plot3D(t, x, y, 'r', label='f(t) = exp(2π2i t)')

# projection
ax.plot3D(t, x, np.zeros_like(t), 'b', label='Проекция на x-t')
ax.plot3D(t, np.zeros_like(t), y, 'g', label='Проекция на y-t')

# set label
ax.set_xlabel('Time')
ax.set_ylabel('Real Axis')
ax.set_zlabel('Imag Axis')
ax.set_title('Комплексная экспонента')

ax.legend()
plt.show()

