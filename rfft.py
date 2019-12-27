from sys import argv
import numpy as np
from math import ceil, pi
import matplotlib.pyplot as plt

def sample(func, t0, t1, fs):
    N = ceil((t1 - t0) * fs)
    t = np.linspace(t0, t1, N)
    return func(t)

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
t_max = 5
assert(name == "sin" or name == "square")
assert(fs > 1 / t_max)
if name == "sin":
    s = sample(sin_wave, 0, 5, fs)
else:
    s = sample(square_wave, 0, 5, fs)
print(s)
fig, [ax1, ax2, ax3] = plt.subplots()
plt.show()
