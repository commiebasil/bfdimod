#!/usr/bin/env python

from PIL import Image
import os
x = input("insert the filename (or all to resize all flags: ")
if x == 'all':
    for file in os.listdir('.'):
        print(file)
        if "." in file:
            if file.split('.')[1] == 'tga':
                image = Image.open(file)
                image.resize((41, 26)).save('medium/'+file)
                image.resize((10, 7)).save('small/'+file)
else:
    for file in os.listdir('.'):
        print(file)
        if "." in file:
            if file == x:
                image = Image.open(file)
                image.resize((41, 26)).save('medium/'+file)
                image.resize((10, 7)).save('small/'+file)
