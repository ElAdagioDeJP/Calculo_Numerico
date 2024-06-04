import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

[x,y,z] = X0 = [0,0,0]
ax.scatter(x, y, z, c='r', marker='o')

plt.show()