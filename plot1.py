import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.sin(x), 'r-')
plt.xlim(0, 2 * np.pi)

plt.savefig('plot1.pdf')
