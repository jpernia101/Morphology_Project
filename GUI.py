from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
from PIL import ImageTk, Image


global img
global label
global imageLocation

def getImage(self):
    curDir = os.getcwd()
    imageLocation = filedialog.askopenfilename(
        initialdir = curDir, title = "Select file", 
        filetypes = (("jpeg files","*.jpg *.jpeg"),("png files","*.png")))

    print(imageLocation)

    img = ImageTk.PhotoImage(file = imageLocation)  #Image.open(imageLocation))
    label = tk.Label(root, image=img).grid(row = 10, column = 0)
    return 


def getImageType(self):
    a = binaryGreyValue.get()
    method = StringVar()
    if a == 2:
        method.set("greyscale")
        #call the greyscale function
    elif a == 1:
        method.set("binary")

    #return the new discolored image    
    return 1



def processImage(self, event):

    #method =
    #description = getDescription(method)
    return



# def getImageMethod(event):
#
# def getDescription(event):




root = Tk()


Label(root, text= "Upload a binary or greyscale image").grid(row=0, column=0, sticky=W)

Label(root, text= "Choose an image type:").grid(row=1, column=0, sticky=W)


binaryGreyValue = IntVar()
#radiobuttons were set with values 1 for binary, and 2 for greyscale, stored in var v
Radiobutton(root, text = "Binary", value = 1, variable = binaryGreyValue, command = getImageType).grid(row = 1, column = 1, sticky = W)
Radiobutton(root, text = "Greyscale", value = 2, variable = binaryGreyValue, command = getImageType).grid(row = 1, column = 2, sticky = W)


Label(root, text= "Choose and Image Morphology Method").grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Erosion", value=3).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Dilation", value=4).grid(row=4, column=0, sticky=W)


loadImageButton = Button(root, text= "Upload Image")
loadImageButton.bind("<Button-1>", getImage)
loadImageButton.grid(row=5, column=0)



# img = ImageTk.PhotoImage(file = "/Users/jeffsando/Desktop/Morphology_Project/cells.png")  #Image.open(imageLocation))
# label = tk.Label(root, image=img).grid(row = 10, column = 0)


# Button(root, text= "Process", command = getImage).grid(row=8, column=0)




description = StringVar()
description.set("Brief explanation of the Image Morphology method")












# processImageButton.bind("<Button-1>", processImage)


# Label(root, text= "Description").grid(row=5, column=1, sticky=W)
# (root, text=description).grid(row=6, column=1, sticky=W)



root.mainloop()
