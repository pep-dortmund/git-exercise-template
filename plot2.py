import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
fig, ax = plt.subplots(1, 1, layout="constrained")

ax.plot(x, np.exp(x), "r-", label=r"$\exp(x)$")

ax.set(
    xlim=(0, 2 * np.pi),
    ylim=(-0.2, None),
    xlabel=(r"$x$"),
    xticks=np.arange(0, 2.1 * np.pi, np.pi / 2),
    xticklabels=(
        [
            r"$0$",
            r"$\frac{1}{2}\pi$",
            r"$\pi$",
            r"$\frac{3}{2}\pi$",
            r"$2\pi$",
        ]
    ),
)

ax.legend()
fig.savefig("plot2.pdf")
