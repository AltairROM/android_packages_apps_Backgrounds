#!/usr/bin/env python3
import os

from PIL import Image

path = os.path.dirname(os.path.realpath(__file__))

resources = "res/drawable-nodpi"

def generate_smallvariants(resource):
    global path
    wallpapers_path = os.path.join(path, resource)
    clean(wallpapers_path)
    wallpapers = os.listdir(wallpapers_path)

    if not hasattr(Image, 'Resampling'):  # Pillow<9.0
        Image.Resampling = Image
    # Now PIL.Image.Resampling.BICUBIC is always recognized.

    for wallpaper in wallpapers:
        # Append _small.jpg to the wallpaper
        wallpaper_small = os.path.splitext(wallpaper)[0] + "_small.jpg"
        wallpaper_small_path = os.path.join(wallpapers_path, wallpaper_small)

        # Save the wallpaper with 1/3 size to wallpaper_small_path
        with Image.open(os.path.join(wallpapers_path, wallpaper)) as img:
            size = int(img.width / 3), int(img.height / 3)

            img_small = img.resize(size, Image.Resampling.LANCZOS)
            img_small.save(wallpaper_small_path, "JPEG")

def clean(wallpapers_path):
    wallpapers = os.listdir(wallpapers_path)

    for wallpaper in wallpapers:
        # Get rid of existing small variants
        if wallpaper.endswith("_small.jpg"):
            os.remove(os.path.join(wallpapers_path, wallpaper))

generate_smallvariants(resources)
