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
data0 = pd.read_csv('Set6_upper.csv', delimiter=',')                     
data1 = pd.read_csv('Set6_lower.csv', delimiter=',')                 


# Creating plot
fig, ax = plt.subplots(1, 1, figsize=(8, 5))

markers = ["o", "o"]
marker_size = 60
color = "k"

Cp = [data0['Cp'], data1['Cp']]

ch_dist = [data0['x/c'], data1['x/c']]



for i in range(len(Cp)):
    ax.scatter(ch_dist[i], Cp[i], marker=markers[i], color=color, s=marker_size, label=r"$\alpha={:1d}^\circ$".format(i))
    cubic_spline = interp1d(ch_dist[i].values, Cp[i].values, kind='cubic')
    ch_dist_spline = np.linspace(np.min(ch_dist[i].values), np.max(ch_dist[i].values), 100)
    if i==0:
        ax.plot(ch_dist_spline, cubic_spline(ch_dist_spline), ls=":", color=color, label="cubic spline")
    else:
        ax.plot(ch_dist_spline, cubic_spline(ch_dist_spline), ls=":", color=color)
        plt.gca().invert_yaxis()
      
fontsize_label = 15
fontsize_label1 = 12
ax.set_xlabel(r"$x/c$", fontsize=fontsize_label1)
ax.set_ylabel(r"$Cp$", fontsize=fontsize_label)
ax.set_title(r'Airfoil surface pressure coefficient (Experimental) for dataset-6',fontsize=fontsize_label1)
#ax.legend()

# save as PDF for general usage, e.g., inclusion in Latex documents
plt.savefig("Airfoil surface pressure coefficient (Experimental) for dataset-6", bbox_inches="tight")
# save as svg for web, e.g., Github, websites, ...
plt.savefig("Airfoil surface pressure coefficient (Experimental) for dataset-6", bbox_inches="tight")
# show for convenience
plt.show()
