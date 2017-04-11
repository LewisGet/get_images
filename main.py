import numpy as np
import pyscreenshot as ImageGrab
import os, time

path = os.sep.join([os.path.expanduser("~lewis"), "Desktop", "logs"])

if __name__ == "__main__":
    for i in range(20 * 60 * 2):
        im = ImageGrab.grab()
        im.save(path + os.sep + "screen." + str(i) + ".bmp")
        time.sleep(0.5)
