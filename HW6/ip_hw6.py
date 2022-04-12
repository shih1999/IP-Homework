"""
Otsu's thresholding method
"""
import skimage.io as io
import numpy as np
import matplotlib.pyplot as plt

def get_histogram(array):
    histogram = np.zeros(256)
    for p in array:
        histogram[int(p)] += 1
    return histogram

def get_sum(head, toe, array):
    sum = 0
    for i in range (head, toe+1):
        sum = sum + array[i]
    return sum

def get_expected(head, toe, array):
    sum = 0
    for i in range (head, toe+1):
        sum = sum + i*array[i]
    return sum

# read image
name = input('Enter image name : ')
filename, filetype = name.split('.')
original_image = io.imread(name)

# get image height, image width
information = original_image.shape
height = information[0]
width = information[1]
size = height*width

# flatten the array (matrix)
flat = original_image.flatten()
# get histogram
histogram = get_histogram(flat)
plt.plot(histogram)
plt.show()

# describe histogram as a probability distribution : pi = ni/N
probability = histogram/size
plt.plot(probability)
plt.show()

L = 256
max_result = -1
best_t = 0

# determine threshold value 
m = get_expected(0, L-1, probability)
for t in range(256):
    at = get_sum(0, t, probability)
    bt = get_sum(t+1, L-1, probability)
    ma = get_expected(0, t, probability)
    if (at != 0  and bt != 0):
        result = pow((ma - m*at),2) / (at*bt)
        if (result > max_result):
            max_result = result
            best_t = t
        
print('final threshold value: ', best_t)    

# thresholding 
new_image = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        if (original_image[i][j] >= best_t):
            new_image[i][j] = 255
        else:
            new_image[i][j] = 0

# show result image
io.imshow(new_image, vmin=0, vmax=255, cmap='gray')
# save result image           
io.imsave(filename + '_output.' + filetype, new_image.astype(np.uint8))