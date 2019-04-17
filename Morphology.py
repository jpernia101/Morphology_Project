#Perform Morphological functions here

#currently just binary, will add otsu/monochrome compatibility

import numpy as np

window = 3

class Morphology:

    def dilate(self, image):
        """Performs dilation on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        [height, width] = image.shape

        

        return image

    def erosion(self, image):
        """Performs erosion on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        return image
    
    def close(self, image):
        """Performs close on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        return image
    
    def open(self, image):
        """Performs open on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        return image

    def close_open(self, image):
        """Performs close open on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        return image

    def open_close(self, image):
        """Performs dilation on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        return image