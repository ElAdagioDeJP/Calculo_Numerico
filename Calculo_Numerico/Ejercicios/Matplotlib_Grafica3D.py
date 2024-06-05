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

# Mostrar la figura
plt.show()