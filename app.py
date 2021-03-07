import sys
import os
from PIL import ImageGrab
import time

window = [int(x.strip()) for x in sys.argv[2].split(',')]
image = ImageGrab.grab(bbox=(window[0] + 3, window[1] + 26, window[2] - 3, window[3] - 3))
image.save(os.path.abspath(sys.argv[1]) + os.sep + str(time.time()) + '.png')