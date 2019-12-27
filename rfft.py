from sys import argv
import numpy as np
from math import ceil, pi
import matplotlib.pyplot as plt

def sample(func, t0, t1, fs):
    N = ceil((t1 - t0) * fs)
    t = np.linspace(t0, t1, N)
    return t, func(t)

def sin_wave(t):
    return 5 * np.cos(2 * pi * t) + 2 * np.sin(3 * pi * t) + 3 * np.cos(5 * pi * t + pi / 6)

def square_wave(t):
    y = []
    D = 0.3
    T = 0.5
    for x in t:
        if x % T < D * T:
            y.append(3.3)
        else:
            y.append(0.0)
    return y

name = argv[1]
fs = float(argv[2])
t_max = 2
assert(name == "sin" or name == "square")
assert(fs > 1 / t_max)
if name == "sin":
    ts, ys = sample(sin_wave, 0, t_max, fs)
    t, y = sample(sin_wave, 0, t_max, 1000)
else:
    ts, ys = sample(square_wave, 0, t_max, fs)
    t, y = sample(square_wave, 0, t_max, 1000)
ys = np.array(ys, dtype=float)
N = ys.size
yf = 2 * np.abs(np.fft.rfft(ys) / N)
f = np.linspace(0, fs / 2, N // 2 + 1)
fig, (ax1, ax2) = plt.subplots(2, 1)
plt.subplots_adjust(wspace =0, hspace =0.6)
ax1.plot(t, y, 'k-')
ax1.plot(ts, ys, 'rx')
ax1.set(title='Time domin', xlabel='second', xlim=[0, t_max])

ax2.stem(f, yf, use_line_collection=True)
ax2.set(title='Freq domin', xlabel='Hz', xlim=[-0.2,fs / 2])
plt.show()
