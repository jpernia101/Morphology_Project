from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
from PIL import ImageTk, Image
import cv2
import Binary
from datetime import datetime



global inputImage
global label
global finalLabel
global imageTypeValue
global funcType


def getImage(self):
    curDir = os.getcwd()
    imageLocation = filedialog.askopenfilename(
        initialdir = curDir, title = "Select file", 
        filetypes = (("jpeg files","*.jpg *.jpeg"),("png files","*.png")))

    #this makes the input image into a matrix
    inputImage = cv2.imread(imageLocation, 0)
    print(inputImage)
    img = ImageTk.PhotoImage(file = imageLocation)  #Image.open(imageLocation))
    label = tk.Label(root, image = img).grid(row = 10, columnspan = 6)
    label.image = img

    return 


def getImageType():
    imageTypeValue = binaryGreyValue.get()
    print(imageTypeValue)
    print("changed value")
    # if imageTypeValue == 2:
    #     method.set("greyscale")
    # elif imageTypeValue == 1:
        # method.set("binary")

    #return the new discolored image    
    return




def getFunctionType():
    print("changing the function")
    funcType = functionTypeValue.get()
    print(funcType)
    return




def makeGreyOrBinary():
    if imageTypeValue == 2: #greyscale
        print("greyscale")
        #greyscale function on the image
    elif imageTypeValue == 1:
        binaryObj = Binary.Binary()
        
        histogram = binaryObj.compute_histogram(inputImage)
        optThreshold = binaryObj.find_optimal_threshold(histogram, inputImage)
        binaryObj.binarize(inputImage, optThreshold)


        print("h")

    return


def runFunction():
    if funcType == 1:
        #Erosion
        print("h")
    elif funcType == 2:
        #Dilation
        print("h")
    elif funcType == 3:
        #Opening
        print("h")
    elif funcType == 4:
        #Closing
        print("h")
    elif funcType == 5:
        #Open-Close
        print("h")
    elif funcType == 6:
        #Close-Open
        print("h")
    elif funcType == 7:
        #Skeletanization
        print("h")
    elif funcType == 8:
        #Boundary Extraction
        print("h")



def processImage(self):
    print("processing")
    if(imageTypeValue == 0 or funcType == 0 or inputImage == []):
        print(imageTypeValue)
        print(funcType)
        print(inputImage)
        print("alert goes here")
        return

    print("function")
    makeGreyOrBinary()
    print("after functions")

    curDir = os.getcwd()

    outputDir = '/output/'

    print(curDir)

    outputImageName = curDir + outputDir + "curImage" + datetime().now().strftime("%m%d-%H%M%S")+".jpg"
    cv2.imwrite(outputImageName, inputImage)    

    finalImage = ImageTk.PhotoImage(file = outputImageName)  #Image.open(imageLocation))
    finalLabel = tk.Label(root, image = finalImage).grid(row = 31, columnspan = 6)
    finalLabel.image = finalImage


    return



# def getImageMethod(event):
#
# def getDescription(event):




root = Tk()


Label(root, text= "Upload a binary or greyscale image").grid(row=0, columnspan = 3, sticky=W)


Label(root, text= "Choose an image type:").grid(row=1, columnspan = 3, sticky=W)
binaryGreyValue = IntVar()
#radiobuttons were set with values 1 for binary, and 2 for greyscale, stored in var v
Radiobutton(root, text = "Binary", value = 1, variable = binaryGreyValue, command = getImageType).grid(row = 2, column = 0, sticky = W)
Radiobutton(root, text = "Greyscale", value = 2, variable = binaryGreyValue, command = getImageType).grid(row = 2, column = 1, sticky = W)


Label(root, text= "Choose an Image Morphology Method").grid(row=3, columnspan = 3, sticky=W)
functionTypeValue = IntVar()
Radiobutton(root, text = "Erosion", value = 1, variable = functionTypeValue, command = getFunctionType).grid(row = 4, column = 0, sticky = W)
Radiobutton(root, text = "Dilation", value = 2, variable = functionTypeValue, command = getFunctionType).grid(row=5, column=0, sticky = W)
Radiobutton(root, text = "Opening", value = 3, variable = functionTypeValue, command = getFunctionType).grid(row = 4, column = 1, sticky = W)
Radiobutton(root, text = "Closing", value = 4, variable = functionTypeValue, command = getFunctionType).grid(row = 5, column = 1, sticky = W)
Radiobutton(root, text = "Open-Close", value = 5, variable = functionTypeValue, command = getFunctionType).grid(row = 4, column = 2, sticky = W)
Radiobutton(root, text = "Close-Open", value = 6, variable = functionTypeValue, command = getFunctionType).grid(row = 5, column = 2, sticky = W)
Radiobutton(root, text = "Skeletinization", value = 7, variable = functionTypeValue, command = getFunctionType).grid(row = 4, column = 3, sticky = W)
Radiobutton(root, text = "Boundary Extraction", value = 8, variable = functionTypeValue, command = getFunctionType).grid(row = 5, column = 3, sticky = W)



loadImageButton = Button(root, text= "Upload Image")
loadImageButton.bind("<Button-1>", getImage)
loadImageButton.grid(row=6, column=0)





processImageButton = Button(root, text = "Process")
processImageButton.bind("<Button-1>", processImage)
processImageButton.grid(row = 30, column = 0, sticky = W)




# description = StringVar()
# description.set("Brief explanation of the Image Morphology method")












# processImageButton.bind("<Button-1>", processImage)


# Label(root, text= "Description").grid(row=5, column=1, sticky=W)
# (root, text=description).grid(row=6, column=1, sticky=W)



root.mainloop()
