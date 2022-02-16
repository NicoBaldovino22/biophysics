# computer-lab-3-9.3-nico-baldovino.py
# Python 5.1
"""
Author:        Nico Baldovino
Created:       Mon Feb 07 12:40:26 2022
Modified:      Sun Feb 13 19:58:03 2022

Description
--------------
The following code consists of the steps explained in Chapter 9 of A Student's Guide to Python
"""
#%% importing np, plt, & intro

import numpy as np
import matplotlib.pyplot as plt
print("\n Hello World! \n Welcome to PHY 307 - Biophysics with Jesse Kinder \
      \n My name is Nico Baldovino  \
       \n The following are the printed results from Chapter 9 in \
        \n A Student's Guide to Python: \n")
        
#%% [working] Section 9.3 - Emphasizing Features

# Part a
v = np.arange(-25,26)
X, Y = np.meshgrid(v, v)
gauss_filter = np.exp(-0.5*((X**2)/2 + (Y**2)/45))

from mpl_toolkits.mplot3d import Axes3D
fig1 = plt.figure('Surface Plot of the Gauss Filter', figsize=(10,8))
gauss = Axes3D(fig1)
gauss.plot_surface(X, Y, gauss_filter, rstride=1, cstride=1)
plt.savefig('Surface Plot of the Gauss Filter.jpg')

# Part b
from scipy.signal import convolve
laplace_filter = np.array( [ [0, -1, 0], [-1, 4, -1], [0, -1, 0] ] )
combined_filter = convolve(gauss_filter, laplace_filter, mode='valid')

fig2 = plt.figure('Surface Plot of the Combined (Laplace & Gaussian) Filter', figsize=(10,8))
combinded_filter = Axes3D(fig2)
combined_filter.plot_surface(X, Y, combined_filter, rstride=1, cstride=1)
plt.title('Combined (Laplace & Gaussian) Filter')

plt.savefig('Surface Plot of the Combined (Laplace & Gaussian) Filter.jpg')