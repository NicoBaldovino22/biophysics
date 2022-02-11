# computer-lab-2-7.3.2.py
# Python 5.1
"""
Author:        Nico Baldovino
Created:       Mon Jan 17 19:58:03 2022
Modified:      Mon Jan 17 19:58:03 2022

Description
--------------
The following code consists of the steps explained in section 7.3.2 of A Student's Guide to Python
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

#%% Section 7.3.2a
num_flips = 1000
xi = 0.08

flips = (rand(num_flips) < xi) * 1
#print(flips)
#x = np.diff(np.nonzero([1, 0, 0, -1])).flatten()
#print(x)
wait_times = np.diff(flips.nonzero()).flatten() +1
#print(wait_times)
max_waits = wait_times.max()

plt.figure("histogram of Wait Time Frequencies for {} flips".format(num_flips), figsize=(12,9))
counts, bin_edges, _ = plt.hist(wait_times, bins=25)
plt.title("Wait Time Frequencies between {} flips when xi = {}".format(num_flips,xi), fontsize=20)
plt.xlabel('\n Wait Time Beween Heads', fontsize=14)
plt.ylabel("Number of Occurances in {} Flips \n".format(num_flips), fontsize=14)
plt.savefig('computer-lab-2-7.3.2a.pdf')

plt.figure("Semilog of Wait Time Frequencies for {} flips".format(num_flips), figsize=(12,9))
plt.semilogy(bin_edges[:-1], counts, 'b.', markersize=10)
plt.title("SemiLog Wait Time Frequencies between {} flips when xi = {}".format(num_flips,xi), fontsize=20)
plt.xlabel('\n Wait Time Beween Heads', fontsize=14)
plt.ylabel("Number of Occurances in {} Flips \n".format(num_flips), fontsize=14)
plt.savefig('computer-lab-2-7.3.2a-SemiLog.pdf')

plt.figure("LogLog of Wait Time Frequencies for {} flips".format(num_flips), figsize=(12,9))
plt.loglog(bin_edges[:-1], counts, 'r.', markersize=10)
plt.title("LogLog Wait Time Frequencies between {} flips when xi = {}".format(num_flips,xi), fontsize=20)
plt.xlabel('\n Wait Time Beween Heads', fontsize=14)
plt.ylabel("Number of Occurances in {} Flips \n".format(num_flips), fontsize=14)
plt.savefig('computer-lab-2-7.3.2a-LogLog.pdf')

#%% Section 7.3.2b
avg1 = wait_times.mean()
print("The Average Wait Time between Heads during {} flips = {:.3f}".format(num_flips, avg1))

#%% Section 7.3.2c
num_flips = 10**6
flips = (rand(num_flips) < xi) * 1
#print(flips)
wait_times = np.diff(flips.nonzero()).flatten() +1
#print(wait_times)
max_waits = wait_times.max()

plt.figure("histogram of Wait Time Frequencies for {} flips".format(num_flips), figsize=(12,9))
counts, bin_edges, _ = plt.hist(wait_times, bins=25)
plt.title("Wait Time Frequencies between {} flips when xi = {}".format(num_flips,xi), fontsize=20)
plt.xlabel('\n Wait Time Beween Heads', fontsize=14)
plt.ylabel("Number of Occurances in {} Flips \n".format(num_flips), fontsize=14)
plt.savefig('computer-lab-2-7.3.2c.pdf')

plt.figure("Semilog of Wait Time Frequencies for {} flips".format(num_flips), figsize=(12,9))
plt.semilogy(bin_edges[:-1], counts, 'b.', markersize=10)
plt.title("SemiLog Wait Time Frequencies between {} flips when xi = {}".format(num_flips,xi), fontsize=20)
plt.xlabel('\n Wait Time Beween Heads', fontsize=14)
plt.ylabel("Number of Occurances in {} Flips \n".format(num_flips), fontsize=14)
plt.savefig('computer-lab-2-7.3.2c-SemiLog.pdf')

plt.figure("LogLog of Wait Time Frequencies for {} flips".format(num_flips), figsize=(12,9))
plt.loglog(bin_edges[:-1], counts, 'r.', markersize=10)
plt.title("LogLog Wait Time Frequencies between {} flips when xi = {}".format(num_flips,xi), fontsize=20)
plt.xlabel('\n Wait Time Beween Heads', fontsize=14)
plt.ylabel("Number of Occurances in {} Flips \n".format(num_flips), fontsize=14)
plt.savefig('computer-lab-2-7.3.2c-LogLog.pdf')

avg2 = wait_times.mean()
print("The Average Wait Time between Heads during {} flips = {:.3f}".format(num_flips, avg2))
print("The Difference between the Average Wait Times for {} and {} flips = {} \n".format(10**6,1000,abs(avg2-avg1)))