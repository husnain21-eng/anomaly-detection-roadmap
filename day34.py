import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

rng = np.random.default_rng(3)
times = pd.date_range("2026-11-01", periods=24 * 7, freq="h")
t = np.arange(len(times))

series = pd.Series(
    100 + 0.1 * t + 20 * np.sin(2 * np.pi * t / 24) + rng.normal(0, 3, len(t)),
    index=times,
)

plot_acf(series, lags=72)
plt.title("Autocorrelation of hourly traffic")
plt.xlabel("Lag (hours)")
plt.tight_layout()

plt.savefig("day34_plot.png")
plt.show()