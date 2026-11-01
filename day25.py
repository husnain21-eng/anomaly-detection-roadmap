import pandas as pd

times = pd.date_range(start="2026-11-01", periods=48, freq="h")
df = pd.DataFrame({"bytes": range(100, 148)}, index=times)

print(df.resample("D").mean())
print(df.resample("D").sum())
print(df.resample("6h").mean())