# computer-lab-2.py
# Python 5.1
"""
Author:        Nico Baldovino
Created:       Mon Jan 17 19:58:03 2022
Modified:      Mon Jan 17 19:58:03 2022

Description
--------------
The following code consists of the steps explained in Chapter 7 of A Student's Guide to Python
"""
#%% importing np, plt, & intro

import numpy as np
import matplotlib.pyplot as plt
print("\n Hello World! \n Welcome to PHY 307 - Biophysics with Jesse Kinder \
      \n My name is Nico Baldovino  \
       \n The following are the printed results from Chapter 7 in \
        \n A Student's Guide to Python: (See Printed Figures)")
        
#%% Section 7.1 - Generating and Plotting Trajectories
#% Part a
from matplotlib.backends.backend_pdf import PdfPages
from numpy.random import default_rng
rng = default_rng()
rand = rng.random

num_steps = 1000

x_step = 2*(rand(num_steps) < 0.5) -1 #Generates 1000 random 'coin flips' or steps between -1 and +1 (heads/tails or positive/negative step)
y_step = 2*(rand(num_steps) < 0.5) -1 
x_final = x_step.cumsum() #cumulatively sums the next value in the array with all previous iteration's values in the array x_step
y_final = y_step.cumsum() 

with PdfPages('computer-lab-2-7.1a-nico-baldovino.pdf') as pdf:  
    plt.figure(figsize = (8,8)) #Creates a figure for chapter 7.1a
    plt.plot(x_final,y_final,'.') #plots the trajectory of randomly generated steps created in for loop above
    plt.title('Plot of the Randomly Generated Walk Trajectory \n') #gives a title to the plot
    plt.xlabel('Trajectory of Steps in the X-Direction') #gives an x-axis label to the plot
    plt.ylabel('Trajectory of Steps in the Y-Direction') #gives a y-axis label to the plot 
    plt.axis('square') #makes sure the axis boundaries are square between the x and y axis
    plt.axis('equal') #makes sure the axis labels are equal between the x and y axis
    pdf.savefig()  #saves figure 1 as a .pdf file in our working directory 
    plt.close()
    
#% Part b

M, N = 2, 2
fig, ax = plt.subplots(M, N, sharex=True, sharey=True, figsize=(8,8))

for i in range(M):
    for j in range(N):
        x_step = 2*(rand(num_steps) < 0.5) -1 #Generates 1000 random 'coin flips' or steps between -1 and +1 (heads/tails or positive/negative step)
        y_step = 2*(rand(num_steps) < 0.5) -1 
        x_final = x_step.cumsum() #cumulatively sums the next value in the array with all previous iteration's values in the array x_step
        y_final = y_step.cumsum() 
        ax[i,j].plot(x_final,y_final,'b.')

with PdfPages('computer-lab-2-7.1b-nico-baldovino.pdf') as pdf:  
    fig.suptitle("\n Four Different Randomly Generated Trajectories Plotted Side By Side") #gives a title to the entire subplot in figure 2
    fig.supxlabel("x - direction")
    fig.supylabel("y - direction")
    pdf.savefig() #saves figure 2 as a .pdf file in our working directory
    plt.close()

#%% Section 7.2 - Plotting the Displacement Distribution
# Part a

num_steps = 1000
num_walks = 1000
x_final = np.zeros(num_walks)
y_final = np.zeros(num_walks)
disp = np.zeros(num_walks)
for n in range(num_walks):
    x_step = 2*(rand(num_steps) < 0.5) -1
    y_step = 2*(rand(num_steps) < 0.5) -1 
    x = x_step.cumsum() #cumulatively sums the next value in the array with all previous iteration's values in the array x_step
    y = y_step.cumsum() 
    x_final[n] = x[-1]
    y_final[n] = y[-1]
    disp[n] = np.sqrt(x[-1]**2 + y[-1]**2)

with PdfPages('computer-lab-2-7.2-nico-baldovino.pdf') as pdf:  
    plt.figure(figsize = (8,8))
    plt.scatter(x_final,y_final)
    plt.title('Scatter Plot of the 1000 Different Walks')
    plt.xlabel('X - Direction')
    plt.ylabel('Y - Direction')
    plt.axis('square')
    plt.axis('equal')
    pdf.savefig()
    plt.close()

    # Part b
    plt.figure(figsize = (8,8))
    plt.hist(disp,bins=20)
    plt.title('Displacement in Steps Generated from the 1000 Random Walks')
    plt.xlabel('Number of Steps')
    plt.ylabel('Frequency')
    pdf.savefig()
    plt.close()
    
    # Part c
    plt.figure(figsize = (8,8))
    plt.hist(disp**2,bins=20)
    plt.title('Squared Displacement in Steps Generated from the 1000 Random Walks')
    plt.xlabel('Number of Steps')
    plt.ylabel('Frequency')
    pdf.savefig()
    plt.close()
    
    # Part d
    plt.figure(figsize = (8,8))
    plt.semilogy(disp**2,'b-')
    plt.title('Semilog Representation of the Displacement')
    plt.xlabel('Steps')
    plt.ylabel('Frequency')
    pdf.savefig()
    plt.close()

    plt.figure(figsize = (8,8))
    plt.loglog(disp**2)
    plt.title('Loglog Representation of the Displacement')
    plt.xlabel('Steps')
    plt.ylabel('Frequency')
    pdf.savefig()
    plt.close()
    
# Part e
mean = np.mean(disp**2) #This gives us the mean square displacement of the random walk of 1000 steps
print('\n The Mean Square Difference of the Random Walk of 1000 Steps =',mean)

# Part f
num_steps = 4000
num_walks = 1000
x_final = np.zeros(num_walks)
y_final = np.zeros(num_walks)
disp = np.zeros(num_walks)
for n in range(num_walks):
    x_step = 2*(rand(num_steps) < 0.5) -1
    y_step = 2*(rand(num_steps) < 0.5) -1 
    x = x_step.cumsum() #cumulatively sums the next value in the array with all previous iteration's values in the array x_step
    y = y_step.cumsum() 
    x_final[n] = x[-1]
    y_final[n] = y[-1]
    disp[n] = np.sqrt(x[-1]**2 + y[-1]**2)

with PdfPages('computer-lab-2-7.2f-nico-baldovino.pdf') as pdf:      
    plt.figure(figsize = (8,8))
    plt.scatter(x_final,y_final)
    plt.title('Scatter Plot of the 4000 Step Walk')
    plt.xlabel('X - Direction')
    plt.ylabel('Y - Direction')
    plt.axis('square')
    plt.axis('equal')
    pdf.savefig()
    plt.close()
    
    plt.figure(figsize = (8,8))
    plt.hist(disp,bins=20)
    plt.title('Displacement in Steps Generated from the 1000 Random Walks')
    plt.xlabel('Number of Steps')
    plt.ylabel('Frequency')
    pdf.savefig()
    plt.close()
    
    # Part c
    plt.figure(figsize = (8,8))
    plt.hist(disp**2,bins=20)
    plt.title('Squared Displacement in Steps Generated from the 1000 Random Walks')
    plt.xlabel('Number of Steps')
    plt.ylabel('Frequency')
    pdf.savefig()
    plt.close()
    
    # Part d
    plt.figure(figsize = (8,8))
    plt.semilogy(disp**2,'b-')
    plt.title('Semilog Representation of the Displacement')
    plt.xlabel('Steps')
    plt.ylabel('Frequency')
    pdf.savefig()
    plt.close()
    
    plt.figure(figsize = (8,8))
    plt.loglog(disp**2)
    plt.title('Loglog Representation of the Displacement')
    plt.xlabel('Steps')
    plt.ylabel('Frequency')
    pdf.savefig()
    plt.close()
    
mean = np.mean(disp**2) #This gives us the mean square displacement of the random walk of 4000 steps
print('\n The Mean Square Difference of the Random Walk of 4000 Steps =',mean)