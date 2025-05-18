#!/usr/bin/env python

from PIL import Image
import os
i = input("Insert filename: ")
for file in os.listdir('.'):
	print(file)
	if "." in file:
		if file == i:
			image = Image.open(file)
			image.resize((259, 176)).save(file)
			image = Image.open(file)
			image.crop((25, 0, 234, 176)).save(file)