#Compute histogram and then threshold
#this includes regular (for now), and then bimodal for optimization, and otsu for greyscale

import numpy as np

class Monochrome:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        #initially filling the histogram
        hist = [0]*256
        counter = 0
        for i in range(0,np.size(image,0)):
            for j in range(0,np.size(image,1)):
                hist[image[i][j]] += 1
                counter += 1
            
        norm_hist = [0]*256
        expected_value = 0
        #normalizing histogram and getting expected overall value
        for k in range(0,np.size(hist)):
            norm_hist[k] = hist[k]/counter
            expected_value += (k * norm_hist[k])
                
        return norm_hist