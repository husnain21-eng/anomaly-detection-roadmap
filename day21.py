import pandas as pd

# A Series: one column of values
traffic = pd.Series([120, 135, 128, 150, 162])
print(traffic)
print("Mean:", traffic.mean())

# A DataFrame: a table with 3 columns
df = pd.DataFrame({
    "hour": [1, 2, 3, 4, 5],
    "bytes": [120, 135, 128, 150, 162],
    "packets": [10, 12, 11, 14, 15],
})
print(df)
print(df.shape)