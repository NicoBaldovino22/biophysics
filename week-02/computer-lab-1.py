# computer-lab-1.py
# Python 5.1.5
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

#%% First Computer Lab 5.1 HIV Example
#5.1.1

time = np.linspace(0,10,101) #creating time matrix consisting of 101 numbers counting from 0 to 10

B = 0 #initial viral load
A = 10 #initial viral load
alpha = 10 #rate at which new cells are infected
beta = 10 #rate at which virions are removed from the blood

#formula for virus concentration in patient
viral_load = (A*np.exp(-alpha*time))+(B*np.exp(-beta*time)) #total viral load

#plotting eperimental equation
plt.plot(time, viral_load) #plotting time vs viral load

#%% Fit Experimental Data
#5.1.2

#loading the data set array from current workspace directory
hiv_data = np.loadtxt("HIVseries.csv", delimiter=',') #loading data set HIVseries.csv
np.set_printoptions(suppress=True)

#Slicing each column of the array retrieved from HIVseries.csv into individual arrays for plotting
N = np.size(hiv_data,0) #sizing the array called from HIVseries.csv
time = hiv_data[0:N:1, 0] #first is the time in days since administration of a treatment to an HIV positive patient
concentration = hiv_data[0:N:1, 1] #the second contains the concentration of virus in that patient's blood, in arbitrary units

## Plotting the retrieved data onto a figure
#remember that the experimental formulation is also plotted from 5.1.1 from earlier
plt.plot(time, concentration) #plotting the data arrays
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100}) #resizing the figure
plt.xlabel('Time (days)') #x-axis label
plt.ylabel('Viral Load Concentration') #y-axis label
plt.title('Concentration of Virus in Patients Blood Over Time in Days') #figure title

#%% Assignment
# Part a

