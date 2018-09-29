import numpy as np
from PIL import Image
from ProgressBar import ProgressBar
from ASCII_art_generator import ASCII_art_generator
from numba import jit, prange
from Layers import Layers
import time
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

img = np.array(Image.open(input_file).convert("RGB"))
# img = (img[:,:,0] + img[:,:,1] + img[:,:,2])//3

img_dim = np.shape(img)

print(img_dim)
layer_size = 5
layer_dim = (5,5)
output_dim = (img_dim[0]-layer_dim[0], img_dim[1]-layer_dim[1])


layer = Layers.layer_diagonal()

output = np.zeros( output_dim )
reduced_output = np.zeros( (output_dim[0]//10, output_dim[1]//10) )
reduced_output_dim = np.shape(reduced_output)

bar = ProgressBar(output_dim[0]-1, 1)

@jit(nopython=True)
def do_stuff(output, output_dim):
    for i in range(output_dim[0]):
        for j in range(output_dim[1]):
            output[i,j] += np.sum(layer*img[i:i+5, j:j+5, 0])
            output[i,j] += np.sum(layer*img[i:i+5, j:j+5, 1])
            output[i,j] += np.sum(layer*img[i:i+5, j:j+5, 2])
    return output

t1 = time.clock()
output = do_stuff(output, output_dim)
t2 = time.clock()
print("Time used: %ss" % (t2-t1))

output[output < 0] = 0
output = output/np.max(output)*256
output = output.astype("uint8")

new_img = Image.fromarray(output.astype("uint8"), "P")
new_img.save(output_file)
