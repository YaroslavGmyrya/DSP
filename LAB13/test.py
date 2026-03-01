import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, firwin

# Создаем простой FIR фильтр (фильтр низких частот)
num_taps = 64  # количество коэффициентов
cutoff = 0.2   # частота среза (нормализованная: 0.5 = частота Найквиста)
b = firwin(num_taps, cutoff)  # коэффициенты фильтра

# Вычисляем частотную характеристику
w, h = freqz(b)

# Визуализация
plt.figure(figsize=(10, 6))

# АЧХ (амплитудно-частотная характеристика)
plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(abs(h)))  # в dB
plt.title('Амплитудно-частотная характеристика')
plt.ylabel('Амплитуда (dB)')
plt.grid(True)

# ФЧХ (фазо-частотная характеристика)
plt.subplot(2, 1, 2)
plt.plot(w, np.unwrap(np.angle(h)))  # развернутая фаза
plt.title('Фазо-частотная характеристика')
plt.xlabel('Частота [рад/отсчет]')
plt.ylabel('Фаза (радианы)')
plt.grid(True)

plt.tight_layout()
plt.show()