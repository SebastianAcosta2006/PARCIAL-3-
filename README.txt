comparacion de calcular la serie fourier iterativa y recursiva 

calcular serie fourier iterativa
python
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



calcular serie fourier recursiva
python
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

graficas o tablas de tiempo de ejecucion
python

import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

funcion periodica onda cuadrada
T = 2 * np.pi
t = np.linspace(0, T, 1000, endpoint=False)
f = np.sign(np.sin(t))

funcion de comparacion
def comparar_tiempos(f, t, T, N_vals):
    tiempos_iter = []
    tiempos_rec = []
    for N in N_vals:
        start = timer()
        calcular_serie_fourier_iterativa(f, t, T, N)
        tiempos_iter.append(timer() - start)

        start = timer()
        calcular_serie_fourier_recursiva(f, t, T, N)
        tiempos_rec.append(timer() - start)
    return tiempos_iter, tiempos_rec

N_vals = [5, 10, 20, 30, 40, 50]
tiempos_iter, tiempos_rec = comparar_tiempos(f, t, T, N_vals)

mostrar grafica 
plt.plot(N_vals, tiempos_iter, label="Iterativo", marker='o')
plt.plot(N_vals, tiempos_rec, label="Recursivo", marker='x')
plt.xlabel("Número de armónicos (N)")
plt.ylabel("Tiempo de ejecución (s)")
plt.title("Comparación de tiempo de ejecución")
plt.legend()
plt.grid(True)
plt.show()
```

analisis comparativo 

cual mrtodo resulta mas eficiente?  
el metodo iterativo es mas eficiente.

Por qué? 
el enfoque recursivo genera múltiples llamadas anidadas aumentando la profundidad de pila
tiene una complejidad temporal mayor ya que recalcula todo desde n = 0 hasta n = N cada vez.
el método iterativo solo requiere un buclesin overhead de llamadas
la legibilidad del codigo es mucho más sencillo en el enfoque iterativo que en el recursivo  
La versión recursiva recalcula subproblemas muchas veces y tiene un overhead de llamadas recursivas
la funcion iterativa tiiene mayor profundidad de pila lo que puede generar errores de recursión en valores grandes de N
cpmo tal el enfoque iterativo es lineal y mas facil de entender 

#comparacion iterativo y recursivo 
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

