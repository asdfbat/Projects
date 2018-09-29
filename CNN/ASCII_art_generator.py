import numpy as np
from PIL import Image
import sys
import subprocess
from numba import jit

def wrapper(img_name, max_shape, return_as="array"):
    img_array = reduce_img_BW(img_name, max_shape)
    ascii_art = ASCII_art_generator(img_array, return_as=return_as)
    return ascii_art


def reduce_img(img_name, max_shape):
    img = np.array(Image.open(img_name).convert("RGBA"))
    shape = np.shape(img[:,:,0])
    skips = np.array(shape)//np.array(max_shape)

    if skips[0] == 0 or skips[1] == 0:
        skips = np.array([1,1])
    reduced_shape = shape//(skips)
    img_array = np.zeros( (reduced_shape[0],reduced_shape[1],4) )
    for i in range(reduced_shape[0]):
        for j in range(reduced_shape[1]):
            img_array[i,j] = img[i*skips[0], j*skips[1]]
    return img_array


def reduce_img_BW(img_name, max_shape):
    img = np.array(Image.open(img_name).convert("RGBA"))
    img_BW = (img[:,:,0] + img[:,:,1] + img[:,:,2])//3    # Converting to Black/White
    shape = np.shape(img_BW)

    skips = np.array(shape)//np.array(max_shape)
    if skips[0] == 0 or skips[1] == 0:
        skips = np.array([1,1])
    reduced_shape = shape//(skips)
    img_array = np.zeros(reduced_shape)
    for i in range(reduced_shape[0]):
        for j in range(reduced_shape[1]):
            img_array[i,j] = img_BW[i*skips[0], j*skips[1]]

    return img_array


def ASCII_art_generator(img_array, return_as):
    signs = np.array([ " ", ".", "-", "~", "+", "o", "0", "@" ])
    shape = np.shape(img_array)
    max_brightness = np.max(img_array)
    if return_as == "array":
        ascii_art = np.empty( shape=(shape), dtype=str)
        for i in range(shape[0]):
            for j in range(shape[1]):
                ascii_art[i,j] = signs[ int( (len(signs)-1)*img_array[i,j]/max_brightness) ]
    elif return_as == "string":
        ascii_art = ""
        for i in range(shape[0]):
            for j in range(shape[1]):
                ascii_art += signs[ int( (len(signs)-1)*img_array[i,j]/max_brightness) ]
            ascii_art += "\n"
    return ascii_art




if __name__ == "__main__":
    ascii_art = wrapper("fig1.png", (40,80))
    shape = np.shape(ascii_art)
    for i in range(shape[0]):
        for j in range(shape[1]):
            sys.stdout.write(ascii_art[i,j])
        sys.stdout.write("\n")
    ascii_art_string = wrapper("fig1.png", (40,80), return_as="string")
    sys.stdout.write(ascii_art_string)
