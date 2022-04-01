"""
Generate Gaussian noise
"""
import skimage.io as io
import math, random
import numpy as np
from numpy import log as ln
import matplotlib.pyplot as plt

mean = 0
sigma = math.sqrt(15)

def get_z1(r, phi):
    return sigma * math.cos(2*math.pi*phi) * math.sqrt(-2*ln(r))
def get_z2(r, phi):
    return sigma * math.sin(2*math.pi*phi) * math.sqrt(-2*ln(r))

def ramdom_pair():
    x = random.random()
    y = random.random()
    return x, y
    
def threshold(x):
    if x < 0:
        return 0
    elif x > 255:
        return 255
    else:
        return x;
  
# define height & width  
height = 300
width = 400

# g(x,y) : gray image with same pixel values of 100
image_g = np.zeros((height, width))
image_g[:][:] = 100
# show image
io.imshow(image_g, cmap='gray')
io.show()
# show histogram
plt.hist(image_g.flatten(), 256, [0,256])
plt.show()
# save gray image
io.imsave('gray.jpg', image_g.astype(np.uint8))

# f(x,y) = g(x,y) + n(x,y)
image_f = np.zeros((height, width))
for i in range(height):
    for j in range(width-1):
        r, phi = ramdom_pair()
        z1 = get_z1(r, phi)
        z2 = get_z2(r, phi)
        image_f[i][j] = threshold(image_g[i][j] + z1)
        image_f[i][j+1] = threshold(image_g[i][j+1] + z2)     
# show noisy image
io.imshow(image_f, cmap='gray')
io.show()
# show new histogram
plt.hist(image_f.flatten(), 256, [0,256])
plt.show()
# save noisy image
io.imsave('noisy.png', image_f.astype(np.uint8))