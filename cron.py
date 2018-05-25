import os
from time import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PERIOD_HOURS = 4

picknew = False
with open("lastchange") as f:
    t = float(f.readline())
    if (time() - t) / 60 / 60 >= PERIOD_HOURS:
        picknew = True

if picknew:
    # call the wallpaper-pickr script
    from wallpaper_pickr import *
