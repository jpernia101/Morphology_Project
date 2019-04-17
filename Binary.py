#Compute histogram and then threshold
#this includes regular (for now), and then bimodal for optimization, and otsu for greyscale

import numpy as np

class Binary:

    def expectation(self, arr, index):
        expected_value = 0
        total_elements = np.sum(arr)
        
        for i in range(np.size(arr)):
            expected_value += ((i + index) * (arr[i]/ total_elements))
        
        return expected_value

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

    def find_optimal_threshold(self, hist, image):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = int(len(hist)/2)
        left_arr = hist[:threshold]
        right_arr = hist[threshold:]

        #expected value
        mu_one = self.expectation(left_arr, 0)
        mu_two = self.expectation(right_arr, threshold)
        threshold = (mu_one + mu_two) / 2
        mu_one_prev = 0
        mu_two_prev = 0
        delta_mu_one = mu_one - mu_one_prev
        delta_mu_two = mu_two - mu_two_prev

        while delta_mu_one != 0 and delta_mu_two != 0 :
            mu_one_prev = mu_one
            mu_two_prev = mu_two
            mu_one = self.expectation(left_arr, 0)
            mu_two = self.expectation(right_arr, threshold)
            threshold = int((mu_one + mu_two) / 2)

            left_arr = hist[:threshold]
            right_arr = hist[threshold:]
            
            delta_mu_one = mu_one - mu_one_prev
            delta_mu_two = mu_two - mu_two_prev

        return threshold

    def binarize(self, image, threshold):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()

        for i in range(0, image.shape[0]):
            for j in range(0, image.shape[1]):
                if int(image[i][j]) < threshold:
                    bin_img[i][j] = 255
                else:
                    bin_img[i][j] = 0

        return bin_img