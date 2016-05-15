#!/usr/bin/env python

from PIL import Image
import urllib
import io


def get_average(pic, size):
    rgb = {
        "red": [],
        "green": [],
        "blue": [],
        "average": []
    }

    for i in range(0, size[0]):
        for j in range(0, size[1]):
            rgb["red"].append(pic[i, j][0])
            rgb["green"].append(pic[i, j][1])
            rgb["blue"].append(pic[i, j][2])

    rgb["average"].append(sum(rgb["red"]) / len(rgb["red"]))
    rgb["average"].append(sum(rgb["green"]) / len(rgb["green"]))
    rgb["average"].append(sum(rgb["blue"]) / len(rgb["blue"]))

    # return tuple(rgb["average"])
    value = tuple(rgb["average"])
    print("RGB: " + str(value))
    hexadecimal_convert(rgb)


def hexadecimal_convert(rgb):
    value = "".join(map(chr, rgb["average"])).encode('hex')
    print("Hex: #" + value)


def get(url):
    image = urllib.urlopen(url)
    image_file = io.BytesIO(image.read())
    im = Image.open(image_file)
    pic = im.load()
    size = im.size
    get_average(pic, size)
