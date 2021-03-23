import numpy as np
import pylab as plt
import matplotlib as mpl
import pandas as pd

#data0 = pd.read_csv('Set1_upper.csv', delimiter=',')                     
#data1 = pd.read_csv('Set1_lower.csv', delimiter=',')                    

#Cp_upper = [data0['Cp']] 

#Cp_lower = [data1['Cp']]

#ch_dist_upper = [data0['x/c']]

#ch_dist_lower = [data1['x/c']]


path="yPlus_airfoil_basecase_yGrad-10000.raw"
data = pd.read_csv(path, sep=" ", skiprows=[0, 1], header=None, names=["x", "y", "z", "yPlus"])             # for this refer run/setcase_name/postProcessing/surface/latesttimestep
# normalize x
data.x = data.x / data.x.max()
data_up = data[data.y >= 0]

data_low = data[data.y < 0]


path1="yPlus_airfoil_onlydec_yGrad-5000.raw"
data1 = pd.read_csv(path1, sep=" ", skiprows=[0, 1], header=None, names=["x", "y", "z", "yPlus"])             # for this refer run/setcase_name/postProcessing/surface/latesttimestep
# normalize x
data1.x = data1.x / data1.x.max()
data1_up = data1[data1.y >= 0]

data1_low = data1[data1.y < 0]


path2="yPlus_airfoil_noWF_basecase.raw"
data2 = pd.read_csv(path2, sep=" ", skiprows=[0, 1], header=None, names=["x", "y", "z", "yPlus"])             # for this refer run/setcase_name/postProcessing/surface/latesttimestep
# normalize x
data2.x = data2.x / data2.x.max()
data2_up = data2[data2.y >= 0]

data2_low = data2[data2.y < 0]



fig, ax = plt.subplots(1, 1)
ax.set_ylim(0.0, 50.0)

ax.plot(data_up.x, data_up.yPlus,color='k', linestyle = 'solid', label='Base_case_yGrading-10K_upper')
ax.plot(data_low.x, data_low.yPlus,color='b', linestyle = 'solid', label='Base_case_yGrading-10K_lower')

ax.plot(data1_up.x, data1_up.yPlus,color='k', linestyle = 'dashed', label='decreased_yGrading-5K_upper')
ax.plot(data1_low.x, data1_low.yPlus,color='b', linestyle = 'dashed', label='decreased_yGrading-5K_lower')

ax.plot(data2_up.x, data2_up.yPlus,color='k', linestyle = 'dotted', label='withoutWallFunction_upper')
ax.plot(data2_low.x, data2_low.yPlus,color='b', linestyle = 'dotted', label='withoutWallFunction_lower')


#plt.scatter(ch_dist_upper, Cp_upper, color='k', marker='p', label='Experimental_uppersurface')
#plt.scatter(ch_dist_lower, Cp_lower, color='b', marker='s', label='Experimental_lowersurface')


#ax.scatter(data_up.x, data_up.cp, color='blue', linestyle = 'solid', label='Numerical_uppersuface')
#ax.scatter(ch_dist_upper, Cp_upper, color='blue', linestyle = 'solid', label='Experimental_uppersurface')
#ax.scatter(data_low.x, data_low.cp, color='k', linestyle='solid', linewidth=0.1, label='Numerical_lowersurface')
#ax.scatter(ch_dist_lower, Cp_lower, color='k', marker='s', label='Experimental_lowersurface')

#plt.gca().invert_yaxis()


fontsize_label = 12
fontsize_label1 = 12
ax.set_xlabel(r"$x/c$", fontsize=fontsize_label1)
ax.set_ylabel(r"$yPlus$", fontsize=fontsize_label)
ax.set_title(r'Comparison of yplus distribution for dataset-1',fontsize=fontsize_label1)
ax.legend()

plt.show()


# save as PDF for general usage, e.g., inclusion in Latex documents
plt.savefig("Comparison of yplus distribution for dataset-1", bbox_inches="tight")
# save as svg for web, e.g., Github, websites, ...



# https://stackoverflow.com/questions/45936630/how-to-put-line-plot-and-scatter-plot-on-the-same-plot-in         **imp- to put line and scatter plot in the same graph
plt.savefig("Comparison of yplus distribution for dataset-1", bbox_inches="tight")
# show for convenience
#plt.show() 	
