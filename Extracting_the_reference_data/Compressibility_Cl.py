# Importing the different libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Reading the data from .csv files
data = pd.read_csv('Cl(0)-cl(3).csv',delimiter=',')                     # Reading the Cl data for alpha = 0 to alpha = 3
data1 = pd.read_csv('Cl(4)-Cl(6).csv',delimiter=',')                    # Reading the Cl data for alpha = 4 to alpha = 6


# Assigning different columns of the data into different series
alpha_zero = data['Cl_0']
alpha_one = data['Cl_1']
alpha_two = data['Cl_2']
alpha_three = data['Cl_3']

alpha_four = data1['Cl_4']
alpha_five = data1['Cl_5']
alpha_six = data1['Cl_6']

Mach_number = data['x']
Mach_number1 = data1['x1']



# Plotting
plt.plot(Mach_number,alpha_zero, label='alpha = 0')
plt.plot(Mach_number,alpha_one,label='alpha = 1')
plt.plot(Mach_number,alpha_two,label='alpha = 2')
plt.plot(Mach_number,alpha_three,label='alpha = 3')
plt.plot(Mach_number1,alpha_four,label='alpha = 4')
plt.plot(Mach_number1,alpha_five,label='alpha = 5')
plt.plot(Mach_number1,alpha_six,label='alpha = 6')



plt.legend()
plt.xlabel('Mach Number (M)')
plt.ylabel('Lift Coefficient (CL)')
plt.title('Effect of compressibility on the Lift of the NACA 0012-34 airfoil')


plt.show()

