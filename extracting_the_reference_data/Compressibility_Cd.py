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
data0 = pd.read_csv('cd_alpha_0.csv', delimiter=',')                     # Reading the Cd data for (alpha = 0 to alpha = 4) excluding alpha = 1
data1 = pd.read_csv('cd_alpha_1.csv', delimiter=',')                    # Reading the Cd data for alpha = 5 to alpha = 6
data2 = pd.read_csv('cd_alpha_2.csv', delimiter=',')                          # Reading the Cd data for alpha = 1
data3 = pd.read_csv('cd_alpha_3.csv', delimiter=',') 
data4 = pd.read_csv('cd_alpha_4.csv', delimiter=',') 
data5 = pd.read_csv('cd_alpha_5.csv', delimiter=',') 
data6 = pd.read_csv('cd_alpha_6.csv', delimiter=',') 


# Creating plot
fig, ax = plt.subplots(1, 1, figsize=(8, 5))

markers = ["x", "<", ">", "+", "o", "*", "^"]
marker_size = 60
color = "k"

cd = [data0['Cd_0'], data1['Cd_1'], data2['Cd_2'], data3['Cd_3'], data4['Cd_4'], data5['Cd_5'], data6['Cd_6']]
ma = [data0['x'], data1['x'], data2['x'], data3['x'], data4['x'], data5['x'], data6['x']]

for i in range(len(cd)):
    ax.scatter(ma[i], cd[i], marker=markers[i], color=color, s=marker_size, label=r"$\alpha={:1d}^\circ$".format(i))
    cubic_spline = interp1d(ma[i].values, cd[i].values, kind='cubic')
    ma_spline = np.linspace(np.min(ma[i].values), np.max(ma[i].values), 100)
    if i==0:
        ax.plot(ma_spline, cubic_spline(ma_spline), ls=":", color=color, label="cubic spline")
    else:
        ax.plot(ma_spline, cubic_spline(ma_spline), ls=":", color=color)

fontsize_label = 23
fontsize_label1 = 15
ax.set_xlabel(r"$Ma$", fontsize=fontsize_label1)
ax.set_ylabel(r"$c_d$", fontsize=fontsize_label)
ax.set_title(r'Effect of compressibility on the drag of NACA0012-34 airfoil',fontsize=fontsize_label1)
ax.legend()

# save as PDF for general usage, e.g., inclusion in Latex documents
plt.savefig("cd_over_ma_reference.pdf", bbox_inches="tight")
# save as svg for web, e.g., Github, websites, ...
plt.savefig("cd_over_ma_reference.svg", bbox_inches="tight")
# show for convenience
plt.show()
