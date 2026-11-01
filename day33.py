import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

rng = np.random.default_rng(3)
times = pd.date_range("2026-11-01", periods=24 * 7, freq="h")  # 7 days, hourly
t = np.arange(len(times))

trend = 100 + 0.1 * t  # slow rise
seasonal = 20 * np.sin(2 * np.pi * t / 24)  # daily cycle
noise = rng.normal(0, 3, len(t))

series = pd.Series(trend + seasonal + noise, index=times)

result = seasonal_decompose(series, model="additive", period=24)

result.plot()
plt.tight_layout()
plt.savefig("day33_plot.png")
plt.show()

print("Missing trend values:", result.trend.isna().sum())