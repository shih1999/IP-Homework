"""
Unsharp masking
"""
import skimage.io as io
import numpy as np
import cv2

# read image
name = input('Enter image name : ')
filename, filetype = name.split('.')
original_image = io.imread(name)

# get image height, image width
information = original_image.shape
height = information[0]
width = information[1]

'''
Average filter
'''
n = 3
div = pow(n,2)

def avg_get_pixel(i, j):
    if (i > height-1 or j > width-1 or i < 0 or j < 0):
        return 0
    else:
        return original_image[i][j]

def avg_filter(i, j):
    sum = 0
    mask = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
    for pixel in mask:
        sum += avg_get_pixel(pixel[0], pixel[1])/div
    return sum

avg_image = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        avg_image[i][j] = avg_filter(i, j)

io.imshow(avg_image, cmap='gray')
io.show()

io.imsave(filename + '_average_filter.' + filetype, avg_image.astype(np.uint8))
      
'''
Median filter
'''
def get_median(array):
    array.sort()
    l = len(array)
    if (l%2 != 0):
        position = (l+1)/2-1
        return array[int(position)]
    else:
        position1 = l/2-1
        position2 = l/2
        return ( int(array[int(position1)]) + int(array[int(position2)]) )/2

def med_get_pixel(i, j):
    if (i > height-1 or j > width-1 or i < 0 or j < 0):
        return -1
    else:
        return original_image[i][j]

def med_filter(i, j):
    values = []
    mask = [[i-1, j-1], [i-1, j], [i-1, j+1], [i, j-1], [i, j], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
    for pixel in mask:
        value = med_get_pixel(pixel[0], pixel[1])
        if (value != -1):
            values.append(value)
    return get_median(values)

med_image = np.zeros((height, width))     
for i in range(height):
    for j in range(width):
        med_image[i][j] = med_filter(i,j)

io.imshow(med_image, cmap='gray')
io.show()

io.imsave(filename + '_median_filter.' + filetype, med_image.astype(np.uint8))

'''
Unsharp Masking
'''
k = 0.9

# create mask : subtract
mask_average = original_image - avg_image
mask_median = original_image - med_image

io.imshow(mask_average, cmap='gray')
io.show()
io.imshow(mask_median, cmap='gray')
io.show()

# add mask to image
unsharp_average = original_image + k*mask_average
unsharp_median = original_image + k*mask_median
io.imshow(unsharp_average, cmap='gray')
io.show()
io.imshow(unsharp_median, cmap='gray')
io.show()

# scale mask
unsharp_average = 255* ( (unsharp_average-unsharp_average.min()) / (unsharp_average.max() - unsharp_average.min()) )
unsharp_median = 255* ( (unsharp_median-unsharp_median.min()) / (unsharp_median.max() - unsharp_median.min()) )

io.imsave(filename + '_median_unsharp.' + filetype, unsharp_average.astype(np.uint8))
io.imsave(filename + '_average_unsharp.' + filetype, unsharp_median.astype(np.uint8))