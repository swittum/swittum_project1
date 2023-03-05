import numpy as np
import matplotlib.pyplot as plt

print("Hello World!")

x = np.arange(0, 10, 0.01)
y = np.sin(x)

plt.plot(x, y)
plt.show()
