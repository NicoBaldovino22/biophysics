# computer-lab-3-nico-baldovino.py
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
        
#%% Section 9.1.1 - Python Tools for Image Processing

from scipy.signal import convolve
impulse = np.zeros( (51,51) )
impulse[25,25] = 1.0
plt.imshow(impulse)
my_filter = np.ones( (3,3) ) / 9
response = convolve(impulse, my_filter)
plt.figure('response')
plt.imshow(response)

Response = convolve(impulse, my_filter, mode='valid') #crops the edges of the convolved image and returns only the central portion of the convolved image
plt.figure('Response')
plt.imshow(Response)

#%% Section 9.1.2 - Averaging

plt.close("all") #closing all previous figures

image = plt.imread('bwCat.tif')
image.shape
image.dtype
image[:10, :10]

plt.figure('bwCat.jpg', figsize=(8,8))    # Creates a new figure
plt.imshow(image)          # Shows the photo of the cat
plt.set_cmap('gray')       # Use grayscale for black and white image
plt.axis('off')            # Get rid of axes and tick marks
fig =  plt.gcf()           # Get current figure object
fig.set_facecolor('white') # Sets the background to white
plt.title('Original Image')
plt.imsave('bwCat.jpg', image, cmap='gray') #saves the photo as a .jpg file in current working directory

# Part a
small_filter = np.ones( (3,3) ) / 9 #small square filter
print("9.1.2 Part A: \n" + \
      "It makes sense to choose 1/9 as the value to multiply the 3x3 matrix by because there are a total of 9 squares that will have their \
values added together in this filter, which takes the mean value of the neighboring 8 squares around it plus itself to output a value \
for the resulting filtered image to convolve to. \n")
# Part B
response = convolve(image, small_filter, mode='valid')
plt.figure('response', figsize=(8,8))
plt.imshow(response)
plt.axis('off')
plt.title('Small Square Filter (3x3)')
plt.savefig('Small Square Filter (3x3).jpg')
print("9.1.2 Part B: \n" + 
      "The image becomes less clear or more blury due to the weighted mean fliter that each pixel convoluted through. \n")

#Generating the photos side by side in a subplot for comparison
plt.figure('Small Square Filter (3x3)', figsize=(10,5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.axis('off')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(response)
plt.axis('off')
plt.title('Small Square Filtered Image (3x3)')

plt.savefig('Comparison of Original Image vs Small Square Filtered (3x3).jpg')

#Part C
large_filter = np.ones( (15,15) ) / 225 # Creating the large square filter (15x15) = 225 pixels
response = convolve(image, large_filter, mode='valid')
plt.figure('Large Square Filter (15x15)', figsize=(10,5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.axis('off')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(response)
plt.axis('off')
plt.title('Large Square Filtered Image (15x15)')

plt.savefig('Comparison of Original Image vs large Square Filtered (15x15).jpg')

print("9.1.2 Part C: \n" +
      "The new filter causes the convoluted image to be even more blury because it is taking a weighted average of the neighboring 14 pixels around it \
plus itself to generate the new pixel; rather than the neighboring 8 as in the (3x3) matrix filter. \n")

# Part d


#%% [working on Part c] Section 9.1.3 - Smoothing with a Gaussian

#plt.close("all") #closing all previous figures

# Now we will be looking at a more complex filter, a Gaussian Filter
gauss = np.loadtxt("gauss_filter.csv", delimiter=',')

# Part a
convolution = convolve(image, gauss, mode='valid')
plt.figure('Gaussian Filter', figsize=(8,8))
plt.imshow(convolution)
plt.axis('off')
plt.title('Gaussian Filter')
plt.savefig('Gaussian Filter.jpg')

# Part b
impulse = np.zeros( (51,51) )
impulse[25,25] = 1.0
my_filter = np.ones( (3,3) ) / 9 #small square filter
convo1 = convolve(impulse, gauss, mode='valid')
convo2 = convolve(impulse, my_filter, mode='valid')

plt.figure('Comparison of Gaussian & Small Square Filter on a Single Dot', figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(convo1)
plt.axis('off')
plt.title('Gaussian')

plt.subplot(1,2,2)
plt.imshow(convo2)
plt.axis('off')
plt.title('Small Square')

plt.savefig("Comparison of Gaussian & Small Square Filter on a Single Dot.jpg")

# Part c
#from mpl_toolkits.mplot3d import Axes3D
#ax = Axes3D(plt.figure('Surface Plot'))
#ax.plot_surface(X, Y, Z, impulse, rcount=100, ccount=200)

#%% [working] Section 9.2 - Denoising an Image

#plt.close('all')

# Part a
# Here we want to make a noisey image by multiplying the original image by some random number between 0 to 1
from numpy.random import default_rng
rng = default_rng()
rand = rng.random

noise = np.ones( (1,1) ) * rand()
noisy = convolve(image, noise, mode='valid')

plt.figure('Noisy Image', figsize=(8,8))
plt.imshow(noisy)
plt.title('Noisy Image')
plt.axis('off')
plt.savefig('Noisy Image.jpg')

plt.figure('Comparison of Noisy Image to Original', figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(noisy)
plt.title('Noisy Image')
plt.axis('off')

plt.savefig('Comparison of Noisy Image to Original.jpg')

# Part b
# Convolution of the Noisy Image with the Small Square Filter
SSF = convolve(noisy, small_filter, mode='valid')
plt.figure('Convolution of Noisy Image and Small Square Filter', figsize=(8,8))
plt.imshow(SSF)
plt.title('Convolution of Noisy Image and Small Square Filter')
plt.axis('off')
plt.savefig('Convolution of Noisy Image and Small Square Filter.jpg')

# Convolution of the Noisy Image with the Large Square Filter
LSF = convolve(noisy, large_filter, mode='valid')
plt.figure('Convolution of Noisy Image and Large Square Filter', figsize=(8,8))
plt.imshow(LSF)
plt.title('Convolution of Noisy Image and Large Square Filter')
plt.axis('off')
plt.savefig('Convolution of Noisy Image and Large Square Filter.jpg')

# Convolution of the Noisy Image and the Gaussian Filter
GF = convolve(noisy, gauss, mode='valid')
plt.figure('Convolution of Noisy Image and Gaussian Filter', figsize=(8,8))
plt.imshow(GF)
plt.title('Convolution of Noisy Image and Gaussian Filter')
plt.axis('off')
plt.savefig('Convolution of Noisy Image and Gaussian Filter.jpg')

# Compares all three of the previously generated images
plt.figure('Comparison of the Effects of each Filter on the Noisy Image', figsize=(8,10))
plt.subplot(3,1,1)
plt.imshow(SSF)
plt.title('Convolution of Noisy Image and Small Square Filter')
plt.axis('off')

plt.subplot(3,1,2)
plt.imshow(LSF)
plt.title('Convolution of Noisy Image and Large Square Filter')
plt.axis('off')

plt.subplot(3,1,3)
plt.imshow(GF)
plt.title('Convolution of Noisy Image and Gaussian Filter')
plt.axis('off')

plt.savefig('Comparison of the Effects of each Filter on the Noisy Image.jpg')

print("9.2b: \n" + "Each of the three filters do NOT improve the Noisy Image, they actually make it more blury \
as well as zoom in on the center of the image more and more. The only filter that seems to work the best is the \
small square filter because it takes a smaller average to base the convolved image filter off of.")

# Therefore, we need to figure out why it is not making a noisy image, and why the filters are making it more and more noisy

#%% [working] Section 9.3 - Emphasizing Features



#%% [working] Section 9.4 (T2) - Image Files and Arrays


