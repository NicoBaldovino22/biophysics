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
print("\n Hello World! \n Welcome to PHY 307 - Biophysics with Jesse Kinder \
      \n My name is Nico Baldovino  \
       \n The following are the printed results from section 5.1 in \
        \n A Student's Guide to Python: ")

#%% First Computer Lab 5.1 HIV Example
#5.1.1
# Part a

time = np.linspace(0,10,101) #creating time matrix consisting of 101 numbers counting from 0 to 10

B = 80000 #initial viral load
A = 80000 #initial viral load
alpha = 0.5 #rate at which new cells are infected
beta = 0.5 #rate at which virions are removed from the blood

#formula for virus concentration in patient
viral_load = (A*np.exp(-alpha*time))+(B*np.exp(-beta*time)) #total viral load

#plotting eperimental equation
plt.plot(time, viral_load, 'b-') #plotting time vs viral load

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
print("\n Examine the plot created in 'Fit Experimental Data'")
plt.plot(time, concentration, 'r.') #plotting the data arrays
plt.rcParams.update({'figure.figsize':(10,8), 'figure.dpi':100}) #resizing the figure
plt.xlabel('Time (days)') #x-axis label
plt.ylabel('Viral Load Concentration') #y-axis label
plt.title('Concentration of HIV Virus in Patients Blood Over Time in Days') #figure title

#%% Part C

"The plot created in the previous parts of this code represents the concentration \
 of the HIV Virus present in the patients blood over a course of 10 days. \
 The best fit model that would most accurately represent the data points \
 gathered in the data set HIVseries. This best fit model had a value for \
 alpha = 0.4 Therefore, with a latency period of HIV at about ten years, the \
 inverse relationship of the T-cell infection rate (1/alpha) = 1/0.4 = 2.5 days. \
 comparing this infection rate to the latency period of about ten years, or rather \
 3600 days, the body is effectively fighting off these HIV cells for extended periods \
 of time. This does not indicate that it takes a long time to infect cells, becuse it \
 actually takes about 2.5 days or so for the cells to be infected. The latency period \
 can be considered long because the body is effectively fighting off the virus on its \
 own due to adaptability over extended periods of time."

