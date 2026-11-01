import pandas as pd

df = pd.DataFrame({
    "hour": [1, 2, 3, 4, 5],
    "bytes": [120, 135, 128, 150, 162],
    "packets": [10, 12, 11, 14, 15],
})

print(df["bytes"])
print(df[["hour", "bytes"]])
print(df.loc[2])
print(df.iloc[0])
print(df.loc[1:3, "bytes"])
print(df[df["bytes"] > 140])