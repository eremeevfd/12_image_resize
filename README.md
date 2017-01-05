# Image Resizer

Thank you for using my script for resizing images.

## Purpose

This script gets path to image (positional argument), and some optional arguments:
* scale
* width or height
* output path

And resizes original image. If you give scale, result is obvious.
If you give width or height, other parameter calculates using original scale.
If you give width and height, you get such an image, but you'll be warned if changing original scale.

## Quick start

Download script, unpack it and run with terminal command:  
<code> $ python3 image_resize.py your_picture.jpg </code>

## Usage

<pre>
$ pip install -r requirements.txt
$ python3 image_resize.py -h
usage: image_resize.py [-h] [--output OUTPUT] [--width WIDTH]
                       [--height HEIGHT] [--scale SCALE]
                       input

Resize an image

positional arguments:
  input            path to original image

optional arguments:
  -h, --help       show this help message and exit
  --output OUTPUT  path to resized image
  --width WIDTH    new width of image
  --height HEIGHT  new height of image
  --scale SCALE    new scale of image
</pre>
