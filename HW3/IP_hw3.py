"""
Histogram Equalization (HE) : Discrete cases
"""
import skimage.io as io
import skimage.color as color
import numpy as np
import matplotlib.pyplot as plt

def get_histogram(array):
    histogram = np.zeros(256)
    for p in array:
        histogram[int(p)] += 1
    return histogram

def get_cumulative(array):
    cumulative = np.zeros(256)
    cumulative[0] = array[0]
    for i in range(1, 256):
        cumulative[i] = cumulative[i-1]+array[i]
    return cumulative

# read image
name = input('Enter image name : ')
filename, filetype = name.split('.')
original_image = io.imread(name)

# get image height, image width
information = original_image.shape
height = information[0]
width = information[1]
size = height*width

# check : color image / grayscale image
if (len(information) < 3):     # grayscale image
    is_gray = 1
    I = original_image
else:                       # color image : RGB to GRAY
    is_gray = 0
    plt.hist(original_image[:][0], 256, [0, 256], color = ['blue', 'green', 'red'])
    plt.show()
    if (filetype == 'png'):
        I = color.rgb2gray(color.rgba2rgb(original_image))
    else:
        I = color.rgb2gray(original_image)
    I *= 255
    # show grayscale
    io.imshow(I, cmap='gray')
    io.show()

# flatten the array (matrix)
flat = I.flatten()
# show original histogram
plt.hist(flat, 256, [0,256])
plt.show()

# get histogram
histogram = get_histogram(flat)
plt.plot(histogram)
plt.show()

# get cumulative histogram
cumulative = get_cumulative(histogram)
plt.plot(cumulative)
plt.show()

# get normalized cumulative histogram
normalized = cumulative/size
plt.plot(normalized)
plt.show()

# scale 
normalized*=(256-1)
plt.plot(normalized)
plt.show()

# mapping
image = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        image[i][j] = normalized[int(I[i][j])]
# show new histogram
plt.hist(image.flatten(), 256, [0,256])
plt.show()

# show new image ( grayscale )
io.imshow(image, cmap='gray')
io.show()

if (is_gray == 0):
    new_image = original_image
    for i in range(height):
        for j in range(width):
            if (I[i][j] == 0):
                mul = 0
            else:
                mul = image[i][j]/I[i][j]
            for k in range(3):
                new = original_image[i][j][k]*mul
                if (new > 255):
                    new_image[i][j][k] = 255
                else:
                    new_image[i][j][k] = new
    plt.hist(original_image[:][0], 256, [0, 256], color = ['blue', 'green', 'red'])
else:
    new_image = image 

io.imsave(filename + '_output.' + filetype, new_image.astype(np.uint8))