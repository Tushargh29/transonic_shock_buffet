import numpy as np
import pylab as plt
import matplotlib as mpl
import pandas as pd

data0 = pd.read_csv('Set1_upper.csv', delimiter=',')                     
data1 = pd.read_csv('Set1_lower.csv', delimiter=',')                    

Cp_upper = [data0['Cp']] 

Cp_lower = [data1['Cp']]

ch_dist_upper = [data0['x/c']]

ch_dist_lower = [data1['x/c']]


path="total(p)_coeff_airfoil.raw"
data = pd.read_csv(path, sep=" ", skiprows=[0, 1], header=None, names=["x", "y", "z", "cp"])             # for this refer run/setcase_name/postProcessing/surface/latesttimestep
# normalize x
data.x = data.x / data.x.max()
data_up = data[data.y >= 0]

data_low = data[data.y < 0]




#fig, ax = plt.subplots(1, 1)


plt.plot(data_up.x, data_up.cp,color='k', linestyle = 'solid', label='Numerical_uppersuface')
plt.plot(data_low.x, data_low.cp,color='b', linestyle = 'solid', label='Numerical_lowersuface')
plt.scatter(ch_dist_upper, Cp_upper, color='k', marker='p', label='Experimental_uppersurface')
plt.scatter(ch_dist_lower, Cp_lower, color='b', marker='s', label='Experimental_lowersurface')


#ax.scatter(data_up.x, data_up.cp, color='blue', linestyle = 'solid', label='Numerical_uppersuface')
#ax.scatter(ch_dist_upper, Cp_upper, color='blue', linestyle = 'solid', label='Experimental_uppersurface')
#ax.scatter(data_low.x, data_low.cp, color='k', linestyle='solid', linewidth=0.1, label='Numerical_lowersurface')
#ax.scatter(ch_dist_lower, Cp_lower, color='k', marker='s', label='Experimental_lowersurface')

plt.gca().invert_yaxis()


fontsize_label = 12
fontsize_label1 = 12
plt.xlabel(r"$x/c$", fontsize=fontsize_label1)
plt.ylabel(r"$Cp$", fontsize=fontsize_label)
plt.title(r'Comparison of Experimental and Numerical Cp distribution for dataset-1',fontsize=fontsize_label1)
plt.legend()

plt.show()


# save as PDF for general usage, e.g., inclusion in Latex documents
plt.savefig("Comparison of Experimental and Numerical Cp distribution for dataset-1", bbox_inches="tight")
# save as svg for web, e.g., Github, websites, ...



# https://stackoverflow.com/questions/45936630/how-to-put-line-plot-and-scatter-plot-on-the-same-plot-in         **imp- to put line and scatter plot in the same graph
plt.savefig("Comparison of Experimental and Numerical Cp distribution for dataset-1", bbox_inches="tight")
# show for convenience
#plt.show() 	
