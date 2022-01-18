# computer-lab-1.py
# Python 5.1
"""
Author:        Nico Baldovino
Created:       Mon Jan 17 19:58:03 2022
Modified:      Mon Jan 17 19:58:03 2022

Description
--------------
The following code consists of the steps explained in section 5.1 of A Student's Guide to Python
"""
#%% importing np, plt, & intro
import numpy as np
import matplotlib.pyplot as plt
print("\n Hello World! \n Welcome to PHY 307 - Biophysics with Jesse Kinder \n My name is Nico Baldovino \n The following are the printed results from section 5.1 in \n A Student's Guide to Python: \n")
#%% computer_lab1
time = np.linspace(0,10,101)
print('time = ', time,'\n')

B = 0 #initial viral load
A = 20 #initial viral load
alpha = 5 #rate at which new cells are infected
beta = 3 #rate at which virions are removed from the blood

viral_load = (A*np.exp(-alpha*time))+(B*np.exp(-beta*time)) #total viral load
print('viral_load = ', viral_load)

plt.plot(time, viral_load)
plt.title('Viral Load Count over Time')
#%% Fit Experimental Data
hiv_data = np.loadtxt(HIVseries.csv)