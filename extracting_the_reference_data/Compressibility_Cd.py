# Importing the different libraries
import numpy as np
import pandas as pd
import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

# increase resolution and use Latex rendering
mpl.rcParams['figure.dpi'] = 160
mpl.rc('text', usetex=True)


# Reading the data from .csv files
data = pd.read_csv('Cd(0)-Cd(4).csv', delimiter=',')                     # Reading the Cd data for (alpha = 0 to alpha = 4) excluding alpha = 1
data1 = pd.read_csv('Cd(5)-Cd(6).csv', delimiter=',')                    # Reading the Cd data for alpha = 5 to alpha = 6
data2 = pd.read_csv('Cd(1).csv', delimiter=',')                          # Reading the Cd data for alpha = 1

# Creating plot
fig, ax = plt.subplots(1, 1, figsize=(8, 5))

markers = ["x", "<", ">", "+", "o", "*", "^"]
marker_size = 60
color = "k"

cd = [data['Cd_0'], data2['Cd_1'], data['Cd_2'], data['Cd_3'], data['Cd_4'], data1['Cd_5'], data1['Cd_6']]
ma = [data['x'], data2['x'], data['x'], data['x'], data['x'], data1['x1'], data1['x1']]

for i in range(len(cd)):
    ax.scatter(ma[i], cd[i], marker=markers[i], color=color, s=marker_size, label=r"$\alpha={:1d}^\circ$".format(i))
    cubic_spline = interp1d(ma[i].values, cd[i].values, kind='cubic')
    ma_spline = np.linspace(np.min(ma[i].values), np.max(ma[i].values), 100)
    if i==0:
        ax.plot(ma_spline, cubic_spline(ma_spline), ls=":", color=color, label="cubic spline")
    else:
        ax.plot(ma_spline, cubic_spline(ma_spline), ls=":", color=color)

ax.set_xlabel(r"$Ma$")
ax.set_ylabel(r"$c_d$")
ax.set_title(r'Effect of compressibility on the drag of NACA0012-34 airfoil')
ax.legend()

# save as PDF for general usage, e.g., inclusion in Latex documents
plt.savefig("cd_over_ma_reference.pdf", bbox_inches="tight")
# save as svg for web, e.g., Github, websites, ...
plt.savefig("cd_over_ma_reference.svg", bbox_inches="tight")
# show for convenience
plt.show()
