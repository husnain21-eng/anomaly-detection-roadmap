import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
times = pd.date_range(start="2026-11-01", periods=48, freq="h")
df = pd.DataFrame({"bytes": 100 + rng.normal(0, 10, 48)}, index=times)

df["rolling_mean"] = df["bytes"].rolling(6).mean()

plt.figure(figsize=(10, 5))
plt.plot(df.index, df["bytes"], label="Raw", alpha=0.6)
plt.plot(df.index, df["rolling_mean"], label="Rolling mean (6 h)", linewidth=2)
plt.title("Raw traffic vs rolling mean")
plt.xlabel("Time")
plt.ylabel("Bytes")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("day27_plot.png")
plt.show()