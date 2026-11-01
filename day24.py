import pandas as pd

times = pd.date_range(start="2026-11-01", periods=48, freq="h")
df = pd.DataFrame({"bytes": range(100, 148)}, index=times)

print(df.head())
print(df.index)
print(df.shape)
print(df.loc[pd.Timestamp("2026-11-01 05:00")])
print(df["2026-11-01 08:00":"2026-11-01 10:00"])