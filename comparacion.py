import numpy as np
import matplotlib.pyplot as plt
import time
from memory_profiler import memory_usage
from fourier_iterativo import calcular_serie_fourier_iterativa
from fourier_recursivo import calcular_serie_fourier_recursiva


T = 2 * np.pi
M = 1000
t = np.linspace(0, T, M)
f = lambda t: np.sin(t) + 0.5 * np.sin(3 * t)

if __name__ == '__main__':
    Ns = [100, 200, 300, 400, 500]
    tiempos_iter = []
    tiempos_rec = []
    mem_iter = []
    mem_rec = []

    for N in Ns:
       
        start = time.time()
        mem = memory_usage((calcular_serie_fourier_iterativa, (f, t, T, N)), max_iterations=1)
        tiempos_iter.append(time.time() - start)
        mem_iter.append(max(mem) - min(mem))

        
        start = time.time()
        mem = memory_usage((calcular_serie_fourier_recursiva, (f, t, T, N)), max_iterations=1)
        tiempos_rec.append(time.time() - start)
        mem_rec.append(max(mem) - min(mem))

    
    for i, N in enumerate(Ns):
        print(f"N={N:3d} | Iterativo: {mem_iter[i]:.4f} MiB | Recursivo: {mem_rec[i]:.4f} MiB")

   
    plt.figure(figsize=(8, 5))
    plt.plot(Ns, tiempos_iter, label='Iterativo', color='blue')
    plt.plot(Ns, tiempos_rec, label='Recursivo', color='orange')
    plt.xlabel('Número de armónicos (N)')
    plt.ylabel('Tiempo de ejecución (s)')
    plt.title('Comparación de tiempo: Método iterativo vs recursivo')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
