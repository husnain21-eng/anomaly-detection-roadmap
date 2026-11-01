import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 60, 3000)

periodic = np.sin(t) + np.sin(2 * t)
quasi = np.sin(t) + np.sin(np.sqrt(2) * t)

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

axes[0].plot(t, periodic)
axes[0].set_title("Periodic: sin(t) + sin(2t), ratio 2, repeats exactly")

axes[1].plot(t, quasi, color="tab:orange")
axes[1].set_title("Quasi-periodic: sin(t) + sin(sqrt(2) t), never repeats exactly")
axes[1].set_xlabel("t")

for ax in axes:
    ax.set_ylabel("Signal")

plt.tight_layout()
plt.savefig("day30_plot.png")
plt.show()