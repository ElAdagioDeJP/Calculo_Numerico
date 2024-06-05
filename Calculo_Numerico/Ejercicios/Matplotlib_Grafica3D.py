import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generar una matriz aleatoria
A = np.random.rand(5,5)

# Crear una malla de coordenadas
x = np.arange(A.shape[1])
y = np.arange(A.shape[0])
x, y = np.meshgrid(x, y)

# Crear una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('eje x')
ax.set_ylabel('eje y')
ax.set_zlabel('eje z')
ax.legend()

# Graficar la superficie
ax.plot_surface(x, y, A, cmap='hot')

# Implementar el método de la potencia
def power_iteration(A, v0, tol=1e-6, max_iter=100):
    """
    Calcular el autovalor y autovector dominantes de la matriz A
    utilizando el método de la potencia.
    
    Parámetros:
    A (numpy.ndarray): Matriz cuadrada
    v0 (numpy.ndarray): Vector inicial
    tol (float): Tolerancia de convergencia
    max_iter (int): Número máximo de iteraciones
    
    Retorna:
    float: Autovalor dominante
    numpy.ndarray: Autovector dominante
    """
    v = v0 / np.linalg.norm(v0)
    for i in range(max_iter):
        v_new = A @ v
        lam = np.linalg.norm(v_new)
        v = v_new / lam
        if np.linalg.norm(A @ v - lam * v) < tol:
            return lam, v
    return lam, v

# Ejemplo de uso del método de la potencia
v0 = np.random.rand(A.shape[1])
lam, v = power_iteration(A, v0)
print(f"Autovalor dominante: {lam:.4f}")
print(f"Autovector dominante: {v.T}")

# Mostrar la figura
plt.show()