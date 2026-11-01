import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])

print(a)
print("mean:", a.mean())
print("std:", a.std())
print("sample std:", a.std(ddof=1))
print(a * 2)
print(a + 5)
print(a + b)
print(a[a > 25])