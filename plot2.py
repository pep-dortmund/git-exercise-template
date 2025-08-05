import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
plt.plot(x, np.exp(x), 'r-', label=r'$\exp(x)$')
plt.xlim(0, 2 * np.pi)

plt.legend()

plt.savefig('plot2.pdf')
