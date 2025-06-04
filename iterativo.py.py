import numpy as np

def calcular_serie_fourier_iterativa(f, t, T, N):
    a0 = (2 / T) * np.trapezoid(f(t), t)
    an = []
    bn = []
    for n in range(1, N + 1):
        an_n = (2 / T) * np.trapezoid(f(t) * np.cos(2 * np.pi * n * t / T), t)
        bn_n = (2 / T) * np.trapezoid(f(t) * np.sin(2 * np.pi * n * t / T), t)
        an.append(an_n)
        bn.append(bn_n)
    return a0 / 2, an, bn
