# Importing the different libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Reading the data from .csv files
data = pd.read_csv('Cd(0)-Cd(4).csv',delimiter=',')                     # Reading the Cd data for (alpha = 0 to alpha = 4) excluding alpha = 1
data1 = pd.read_csv('Cd(5)-Cd(6).csv',delimiter=',')                    # Reading the Cd data for alpha = 5 to alpha = 6
data2 = pd.read_csv('Cd(1).csv',delimiter=',')                          # Reading the Cd data for alpha = 1


# Assigning different columns of the data into series
alpha_zero = data['Cd_0']
alpha_one = data2['Cd_1']
alpha_two = data['Cd_2']
alpha_three = data['Cd_3']
alpha_four = data['Cd_4']
alpha_five = data1['Cd_5']
alpha_six = data1['Cd_6']

Mach_number = data['x']
Mach_number1 = data1['x1']
Mach_number2 = data2['x']



# Plotting of Cd curves for different alphas in the same figure
plt.plot(Mach_number,alpha_zero, label='alpha = 0')
plt.plot(Mach_number2,alpha_one,label='alpha = 1')
plt.plot(Mach_number,alpha_two,label='alpha = 2')
plt.plot(Mach_number,alpha_three,label='alpha = 3')
plt.plot(Mach_number,alpha_four,label='alpha = 4')
plt.plot(Mach_number1,alpha_five,label='alpha = 5')
plt.plot(Mach_number1,alpha_six,label='alpha = 6')



plt.legend()
plt.xlabel('Mach Number (M)')
plt.ylabel('Drag Coefficient (CD)')
plt.title('Effect of compressibility on the Drag of the NACA 0012-34 airfoil')


plt.show()

