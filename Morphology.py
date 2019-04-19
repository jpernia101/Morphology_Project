#Perform Morphological functions here

#currently just binary, will add otsu/monochrome compatibility

import numpy as np

class Morphology:

    def dilate(self, image):
        """Performs dilation on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        final_img = image.copy()

        for i in range(0, np.size(image,0) - 1):
            top = i - 1
            bottom = i + 1
            if top < 0:
                top = 0
            if bottom > np.size(image,0):
                bottom = np.size(image,0)

            for j in range(0,np.size(image,1) - 1):
                left = j - 1
                right = j + 1
                if left < 0:
                    left = 0
                if right > np.size(image,1):
                    right = np.size(image,1)
                
                #perform function
                if (image[top][j] or image[bottom][j] or image[i][left] or image[i][right] or image[i][j]) == 255:
                    final_img[i][j] = 255
                else:
                    final_img[i][j] = 0
                
        return final_img

    def erosion(self, image):
        """Performs erosion on input image
        takes as input:
        image: a binary image
        returns: a binary image"""
        
        final_img = image.copy()
         

        for i in range(0, np.size(image , 0) - 1):
            top = i - 1
            bottom = i + 1
            if top < 0:
                top = 0
            if bottom > np.size(image,0):
                bottom = np.size(image,0)

            for j in range(0,np.size(image , 1) - 1):
                left = j - 1
                right = j + 1
                if left < 0:
                    left = 0
                if right > np.size(image,1):
                    right = np.size(image,1)
                
                # print(i)
                # print(top)
                # print(bottom)
                # print(j)
                # print(left)
                # print(right)


                #perform function
                if (image[top][j] and image[bottom][j] and image[i][left] and image[i][right] and image[i][j]) == 255:
                    final_img[i][j] = 255
                else:
                    final_img[i][j] = 0
                
        return final_img
    
    def close(self, image):
        """Performs close on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        final_img  = self.erosion(self.dilate(image))

        return final_img
    
    def open(self, image):
        """Performs open on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        final_img = self.dilate(self.erosion(image))

        return final_img

    def close_open(self, image):
        """Performs close open on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        final_img = self.close(self.open(image))

        return final_img

    def open_close(self, image):
        """Performs dilation on input image
        takes as input:
        image: a binary image
        returns: a binary image"""

        final_img = self.open(self.close(image))

        return final_img