"""
Transform a color image into a grayscale image by I = (R+G+B)/3
"""
import skimage.io as io

# read image
name = input('Enter image name : ')
filename, filetype = name.split('.')
I = io.imread(name)

# get image height, image width, # of image channels
height = I.shape[0]
width = I.shape[1]
channels = I.shape[2]

# output image
io.imsave (filename + '_output.' + filetype, I)

# rgb to grayscale
'''
There may be some overflow error occurred if the sum of R, G, and B is greater
than 255.
To avoid the exception, R, G, and B should be calculated respectively.
'''
for i in range(height):
    for j in range(width):
        avg = I[i][j][0]/3 + I[i][j][1]/3 + I[i][j][2]/3
        for k in range(3):
            I[i][j][k] = avg

# show grayscale image
io.imshow(I)
io.show()

# save grayscale image
io.imsave(filename + '_grayscale.' + filetype, I)