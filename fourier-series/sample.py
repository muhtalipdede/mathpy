import numpy as np
import matplotlib.pyplot as plt

# Periyodik bir sinüs dalgası oluşturalım
T = 2*np.pi
t = np.linspace(0, T, 1000, endpoint=False)
f = np.sin(t)

# Fourier serisini hesaplayalım
n = 10
a0 = 2*np.mean(f)
a = np.zeros(n)
b = np.zeros(n)
for i in range(1, n+1):
    a[i-1] = 2*np.mean(f*np.cos(i*t))/T
    b[i-1] = 2*np.mean(f*np.sin(i*t))/T
fourier = np.zeros_like(t)
for i in range(1, n+1):
    fourier += a[i-1]*np.cos(i*t) + b[i-1]*np.sin(i*t)

# Orjinal fonksiyonu ve Fourier serisini çizdirelim
plt.plot(t, f, label='Orjinal Fonksiyon')
plt.plot(t, a0/2 + fourier, label='Fourier Serisi')
plt.legend()
plt.show()
