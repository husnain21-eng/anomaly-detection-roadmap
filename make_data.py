import os
import pandas as pd

data = {
    "day": list(range(1, 11)),
    "value": [120, 135, 128, 150, 162, 155, 170, 165, 180, 195],
}
pd.DataFrame(data).to_csv("data.csv", index=False)

print("Saved to:", os.path.abspath("data.csv"))
df = pd.read_csv("data.csv")
print(df.columns.tolist())