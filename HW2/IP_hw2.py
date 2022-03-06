import skimage.io as io
import numpy as np

# read image ( grayscale format )
name = input('Enter image name : ')
filename, filetype = name.split('.')
I = io.imread(name, as_gray=True)

# scale image
I*=255

# get image height, image width, image channels
height = I.shape[0]
width = I.shape[1]

"""
part A
"""   

# dithering matrix d1
d1 = [[0, 128, 32, 160],
      [192, 64, 224, 96],
      [48, 176, 16, 144],
      [240, 112, 208, 80]]

# generate a matrix of image size by repeating d1
D1 = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        D1[i][j] = d1[i%4][j%4]
        
# threshold image I
I1 = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        if (I[i][j]>D1[i][j]):
            I1[i][j] = 255
        else:
            I1[i][j] = 0


"""
part B : Extend to n = 4 gray values
"""
# 255/3 = 85
Q = I/85

# dithering matrix d2
d2 = [[0, 56],
      [84, 28]]

# generate a matrix of image size by repeating D2
D2 = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        D2[i][j] = d2[i%2][j%2]
        
# threshold image I
I2 = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        if (I[i][j]-85*Q[i][j] > D2[i][j]):
            I2[i][j] = Q[i][j]+1
            
        else:
            I2[i][j] = Q[i][j]+0
            
# scale image
I2_scale = 255* ( (I2-I2.min()) / (I2.max() - I2.min()))

# show images
io.imshow(I, cmap='gray')
io.show()
io.imshow(I1, cmap='gray')
io.show()
io.imshow(I2_scale, cmap='gray')
io.show()

# save image
io.imsave (filename + '_output.' + filetype, I.astype(np.uint8)) 
io.imsave(filename + '_grayscale1.' + filetype, I1.astype(np.uint8))
io.imsave(filename + '_grayscale2.' + filetype, I2_scale.astype(np.uint8))
