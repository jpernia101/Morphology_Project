"""dip_final_project.py: main file for final project"""

__author__ = "Ser Patrick of House Byrnes, Second of his Name, Champion of the Children Kissed by Fire, and the Oracle of Processed Images"
__email__ = "pbyrnes@uh.edu"
__version__ = "1.0.0"

import cv2
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

import Binary as bi
import Monochrome as mono

#will change with gui implementation
def display_image(window_name, image):
    """A function to display image"""
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)
    cv2.waitKey(0)

def main():
    """The main function that parses input args, calls any of the
    morphological operations"""

    #parse input arguments
    #might change with gui implementation
    from argparse import ArgumentParser

    parser = ArgumentParser()

    parser.add_argument("-i", "--image", dest="image",
                        help="specify the name of the image", metavar="IMAGE")
    parser.add_argument("-t", "--threshold_type", dest="threshold",
                        help="specify if wish to use otsu as thresholding operation", metavar="THRESHOLD TYPE")
    parser.add_argument("-o", "--operation", dest="operaton",
                        help="specify which operation should be performed on binary image", metavar="OPERATION")
    
    args = parser.parse_args()

    #Load image
    if args.image is None:
        print("Please specify the name of image")
        print("use the -h option to see usage information")
        sys.exit(2)
    else:
        image_name = args.image.split(".")[0]
        input_image = cv2.imread(args.image, 0)

    #check if otsu thresholding is requested
    if args.threshold is None:
        print("Using normal threshold for binary")
        threshold = 'normal'
    else:
        threshold = args.mask

    
    bin_img_obj = bi.Binary()
    otsu_img_obj = mono.Monochrome()
    
    if threshold in ['normal']:
        hist = bin_img_obj.compute_histogram(input_image)
        threshold_value = bin_img_obj.find_optimal_threshold(hist,input_image)
        binary_image = bin_img_obj.binarize(input_image,threshold_value)
    else:
        hist = otsu_img_obj.compute_histogram(input_image)

    


    


if __name__ == "__main__":
    main()

    