import pandas as pd

times = pd.date_range(start="2026-11-01", periods=10, freq="h")
df = pd.DataFrame(
    {"bytes": [100, 110, 90, 120, 105, 95, 130, 100, 115, 105]},
    index=times,
)

df["rolling_mean"] = df["bytes"].rolling(3).mean()
print(df)