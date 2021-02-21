import pandas as pd
import matplotlib.pyplot as plt

path="total(p)_coeff_airfoil.raw"
data = pd.read_csv(path, sep=" ", skiprows=[0, 1], header=None, names=["x", "y", "z", "cp"])
# normalize x
data.x = data.x / data.x.max()
# split in lower and upper side
data_up = data[data.y >= 0]
data_low = data[data.y < 0]
# plot example
plt.plot(data_up.x, data_up.cp)
plt.gca().invert_yaxis()
plt.show()

