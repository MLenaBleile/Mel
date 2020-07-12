# Mel

## What is Mel?

Even had the sudden, gripping desire to know whether a photo looks more like a photo of a jellyfish, or like Topology?? Say no more fam, we've got you covered! Melvin, or Mel for short, is a Convolutional Neural Network that can classify between images associated with Topology, and images of jellyfish. 

## Usage
  1. Download weights.h5, predict.py, and environment.yml. Anaconda 3 is required. Alternatively you can install the following packages manually:
    - keras
    - argparser
    - cv2
    - numpy
 2. Put all the files in the same folder. create and activate the environment with:
  > conda env create -f environment.yml -n mel
  > conda activate mel
 
 3. Finally, run the classifier on an image by running the following:
  > python predict.py --data_path pathtoimage.jpg
  
 For example, if you were to also download one of the example photos included here, jelly.jpg, you could put it in the same folder and run:
  > python predict.py --data_path jelly.jpg

....and in case you're wondering, most colour photos of humans look more like jellyfish :)

## Architecture
Melvin is a 29-layer CNN based on MobileNet. The first 5 layers were frozen and the rest were trained for 100 epochs using a batch size of 30, yeilding validation accuracy of 90%. The top layer is a 10-node dense layer with ReLU activation, and 30% dropout. Image augmentation included a shear and zoom of 0.2, as well as horizontal flipping. I used SGD with momentum 0.9 and binary crossentropy loss (sigmoid activation). 

## Data

The data consist of 1892 images scraped from Google (1664 train, 228 test). I hand-filtered the jellyfish photos a bit so that only jellyfish were inputted. I didn't do the same thing for the topology photos though because come on, who tf really knows what "topology" is supposed to look like??? So I just let Google Image search decide that for me.

Anyway. Enjoy Mel. Major props if anyone actually reads this. xthxbye
