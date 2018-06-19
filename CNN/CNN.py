import numpy as np
from PIL import Image

img = np.array(Image.open("fig1.png").convert("RGBA"))
img = (img[:,:,0] + img[:,:,1] + img[:,:,2])//3

img_dim = np.shape(img)
layer_size = 5
layer_dim = (5,5)
output_dim = (img_dim[0]-layer_dim[0], img_dim[1]-layer_dim[1])

layer_vertical = np.array([
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]])

layer_horizontal = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]])


output = np.zeros( output_dim )

print(output)