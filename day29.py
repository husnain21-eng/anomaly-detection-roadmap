import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)

t = np.arange(0, 48)  # hours 0 to 47
clean = 100 + 20 * np.sin(2 * np.pi * t / 24)
noisy = clean + rng.normal(0, 4, 48)

plt.figure(figsize=(10, 5))
plt.plot(t, noisy, label="Signal + noise")
plt.plot(t, clean, label="Clean sine wave", linestyle="--")
plt.title("Sine wave with noise")
plt.xlabel("Hour")
plt.ylabel("Bytes")
plt.legend()
plt.tight_layout()

plt.savefig("day29_plot.png")
plt.show()