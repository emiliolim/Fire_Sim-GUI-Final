from PIL import Image, ImageEnhance
import numpy as np
from matplotlib import cm
import sys
from math import sqrt

np.set_printoptions(threshold=sys.maxsize)

class Ret:
    def ret_arr(num_pixels, path, show = False):
        road = (245,35,93)
        parking = (135,145,148)
        trees = (137,159,68)
        trees_dark= (24,35,33)
        buildings = (245,245,245)
        water = (255,0,214)
        light_water = (88,183,135)
        blue_parking = (43,58,67)

        COLORS = (
            road,
            trees,
            buildings,
            water,
            parking,
            # blue_parking,
            trees_dark,
            light_water,
        )

        def closest_color(rgb):
            r, g, b = rgb
            color_diffs = []
            for color in COLORS:
                cr = color[0]
                cg = color[1]
                cb = color[2]
                color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
                color_diffs.append((color_diff, color))
            return min(color_diffs)[1]

        
        im = Image.open(path)
        width, height = im.size   # Get dimensions

        new = 512*3

        left = (width - new)/2
        top = (height - new)/2
        right = (width + new)/2
        bottom = (height + new)/2

        # Crop the center of the image
        im = im.crop((left, top, right, bottom))
        l,w = im.size
        print( l,w)

        enhancer = ImageEnhance.Contrast(im)
        im = enhancer.enhance(1.3)

        # sys.exit("Error message")

        imgSmall = im.resize((num_pixels,num_pixels), resample=Image.Resampling.BILINEAR)
        # imgSmall.show()

        im_ar = np.asarray(imgSmall)
        im_arr = np.array(im_ar)

        # im_arr.setflags(write=1)
        # print(im_arr)
        print(np.shape(im_arr))
        test = Image.fromarray(np.uint8(im_arr))

        print("running...")
        for i, row in enumerate(im_arr):
            for j, col in enumerate(row):
                rgb =[0,0,0]
                rgb[0] = col[0]
                rgb[1] = col[1]
                rgb[2] = col[2]
                for iter in range(0,3):
                    # im_arr[i][j][iter] = closest_color(rgb)[iter]
                    np.put(im_arr[i][j], iter,closest_color(rgb)[iter] )

        test = Image.fromarray(np.uint8(im_arr))

        if show: test.resize(im.size, Image.Resampling.NEAREST).show()
        



        # pixelated = imgSmall.resize(im.size, Image.Resampling.NEAREST)
        return im_arr

