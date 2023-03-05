import numpy as np
import matplotlib.pyplot as plt

print("Hello World!")

x = np.arange(0, 10, 0.01)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, label="sin(x)")
plt.plot(x, z, label="cos(x)")
plt.legend(loc="best")
plt.grid(True)
plt.show()
