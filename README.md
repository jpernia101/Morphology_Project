# Digital Image Processing

Final Project

Due: Sometime (cant be bothered to look it up)

---

1. Binary:

   a. A program to binarize a grey-level image.

   - expectation: a utility function used for threshold computation
   - compute_histogram: by taking in a grey-level image compute the histogram and return a list holding it
   - find_optimal_threshold: compute optimal threshold from the histogram
   - binarize: Using the threshold, a binarized image should be created.

2. Otsu:
   _TBD_

   a. A different type of algo to binarize an image.

   - most likely the same as the binary class but uses calculations for weight, mean, and variance between the background and foreground
   - honestly might just delete this and add it to the binary class file

3. Morphology:

   a. A program to apply any of six morphological operations on an image by using a 5 pixel cross window, to which all will return a new binary image

   - dilation: Uses OR operations
   - erosion: Uses AND operations
   - close: Uses erosion(dilation())
   - open: Uses dilation(erosion())
   - close_open: Uses close(open())
   - open_close: Uses open(close())

4. Skeleton:
   _this section should be updated_

   a. A program to determine the skeleton of the image.
   b. Also used to perform boundary extraction

5. GUI:
   _this section should be updated_

   a. Implementation of GUI to use all above functions for use

---

How to run the code?

    - dunno, depends on how the gui is working

---

<sub><sup>License: Property of his majesty: King Patrick of House Byrnes, Second of his Name, Champion of the Children Kissed by Fire, and the Oracle of Processed Images.
This software is the property of his majesty, and should not be distributed, reproduced, or shared online, without the permission of his majesty. In order to gain permission, a tax will be levied to the chosen few who can prove their worthiness. I am a generous king.
The contents are not to be reproduced and shared with anyone with out the permission of the King.
The contents are not to be posted on any online public hosting websites without the permission of the King.
The software is cloned and is available to the subjects for the duration of the project.
At the end of the project, all rights shall be retained by his majesty.</sub></sup>
