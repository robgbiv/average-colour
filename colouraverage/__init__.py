#!/usr/bin/env python

# Adapted from http://stackoverflow.com/a/5365853 until...
import os, sys
from PIL import Image

im = Image.open("img/aKvPvwF.jpg")
pic = im.load()
# ...here
size = im.size
red = []
green = []
blue = []
average = []

for i in range(0, size[0]):
  for j in range(0, size[1]):
    red.append(pic[i,j][0])
    green.append(pic[i,j][1])
    blue.append(pic[i,j][2])

average.append(sum(red) / len(red))
average.append(sum(green) / len(green))
average.append(sum(blue) / len(blue))

print tuple(average)
