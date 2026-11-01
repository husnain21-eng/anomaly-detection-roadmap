import pandas as pd
import numpy as np

df = pd.DataFrame({
    "hour": [1, 2, 3, 4, 5, 6],
    "bytes": [120, 135, np.nan, 150, np.nan, 170],
})

print(df)
print(df.isna())
print(df.isna().sum())
print(df.dropna())
print(df.fillna(0))
print(df.fillna(df["bytes"].mean()))