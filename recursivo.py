import numpy as np

def calcular_serie_fourier_recursiva(f, t, T, N, n=1, an=None, bn=None):
    if an is None:
        an = []
    if bn is None:
        bn = []
    if n > N:
        a0 = (2 / T) * np.trapezoid(f(t), t)
        return a0 / 2, an, bn
    an_n = (2 / T) * np.trapezoid(f(t) * np.cos(2 * np.pi * n * t / T), t)
    bn_n = (2 / T) * np.trapezoid(f(t) * np.sin(2 * np.pi * n * t / T), t)
    return calcular_serie_fourier_recursiva(f, t, T, N, n + 1, an + [an_n], bn + [bn_n])
