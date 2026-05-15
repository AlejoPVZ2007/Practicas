import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

t = np.linspace(0, 24 * np.pi, 5000)
r = np.exp(np.sin(t)) - 2 * np.cos(4 * t
        ) + np.sin((2*t - np.pi) /24) ** 5
x = r * np.cos(t)
y = r * np.sin(t)
z = np.sin(t/2) * 3

ax.plot(x, y, z, color='magenta', 
        linewidth=1, alpha=0.7)
ax.set_axis_off()
plt.show()