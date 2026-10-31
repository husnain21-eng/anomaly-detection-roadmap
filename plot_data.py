import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

plt.plot(df["day"], df["value"], marker="o")
plt.title("Daily Value")
plt.xlabel("Day")
plt.ylabel("Value")

plt.savefig("plot.png")
plt.show()