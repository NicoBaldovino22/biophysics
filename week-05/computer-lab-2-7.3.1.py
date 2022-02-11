# computer-lab-2-7.3.1.py
# Python 5.1
"""
Author:        Nico Baldovino
Created:       Mon Jan 17 19:58:03 2022
Modified:      Mon Jan 17 19:58:03 2022

Description
--------------
The following code consists of the steps explained in section 7.3.1 of A Student's Guide to Python
"""
#%% importing np, plt, & intro
import numpy as np
import matplotlib.pyplot as plt
print("\n Hello World! \n Welcome to PHY 307 - Biophysics with Jesse Kinder \
      \n My name is Nico Baldovino  \
       \n The following are the printed results from section 7.3.1 in \
        \n A Student's Guide to Python: \n")
        
#%% importing random number generation
from numpy.random import default_rng
rng = default_rng()
rand = rng.random

#%% Section 7.3.1a
#Before flipping the coins, generate a plot of the Poisson's Distributions for some range of values 'l'
from scipy.special import factorial
l = np.arange(50, dtype='float') # There's no need to lake 'l' all the way to infinity; therefore, it is finite
num_flips = 100
mu = 8
xi = 0.08
Poisson = (np.exp(-mu) * (mu**l)) / factorial(l)
#print("Poisson = {} \n".format(Poisson))

plt.figure('Poissons Dist')
plt.plot(l, Poisson, 'r-', markersize=5, markeredgewidth=2)
plt.title("Poissons Distribution of {} Flips of Heads".format(mu), fontsize=20)
plt.xlabel('Number of Heads Flipped', fontsize=14)
plt.ylabel('Probability', fontsize=14)
plt.savefig('computer-lab-2-7.3.1a-nico-baldovino.pdf')

#%% Section 7.3.1b,c
N = 1000 # Perform N = 1000 flip trials, each consisting of l = 100 flips, that lands heads only 0.08 of the time (8%)
flips = (rand( (num_flips, N) ) < xi) *1  # where heads = 1 = True and tails = 0 = False
#print('\n', flips)
heads = flips.sum(0)
#print('\n', heads)
plt.figure('Hist of Heads')
count, bin_edges, _ = plt.hist(heads, bins=20, range=(0,20))
#print("the number of total heads in each bin = {} \n".format(count))
plt.title("Poisson Distribution with xi = {}".format(xi), fontsize=20)
plt.xlabel('Total Heads Flipped in Each Trial', fontsize=14)
plt.ylabel("Number of Occurances in {} trials".format(N), fontsize=14)
plt.savefig('computer-lab-2-7.3.1bc-nico-baldovino.pdf')

#%% Section 7.3.1d
#% comparison between theoretical and practical (simulated) Poisson Distributions
plt.figure('comparison of theoretical and prcatical Poisson for N = 1000')
count, bin_edges, _ = plt.hist(heads, bins=20, range=(0,20), label='practical')
offset = 0.5*(bin_edges[1]-bin_edges[0]) # in order to make up for the offset of the two generated graphs, centering both on a mutual center
plt.plot(l + offset, Poisson * N, 'r-', label='theoretical')
plt.title("Poisson Process with xi = {}".format(xi), fontsize=20)
plt.xlabel('Total Heads Flipped in Each Trial', fontsize=14)
plt.ylabel("Number of Occurances in {} trials".format(N), fontsize=14)
plt.legend(loc='upper right')
plt.savefig('computer-lab-2-7.3.1d-nico-baldovino.pdf')

#%% Section 7.3.1e
#% repeating steps b through d from N = 1000000 = 10**6

N = 10**6
heads = np.zeros(N)
for i in range(N):
    heads[i] = np.sum(rand(num_flips) < xi)
    
plt.figure('comparison of theoretical and practical Poisson for N = 10^6')
count, edge_bins, _ = plt.hist(heads, bins=20, range=(0,20), label='practical')
offset = 0.5*(edge_bins[1]-edge_bins[0])
plt.plot(l + offset, Poisson * N, 'b-', label='Theoretical')
plt.title("Poisson Process with xi = {}".format(xi), fontsize=20)
plt.xlabel('Total Heads Flipped in Each Trial', fontsize=14)
plt.ylabel("Number of Occurances in {} trials".format(N), fontsize=14)
plt.legend(loc='upper right')
plt.savefig('computer-lab-2-7.3.1e-nico-baldovino.pdf')
