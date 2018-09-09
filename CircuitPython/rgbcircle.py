import time
import random
from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.1

neopixels = [0,1,2,3,4,5,6,7,8,9]
count = 0
while True:
    for pix in neopixels:
        R = random.randrange(0, 255)
        G = random.randrange(0, 255)
        B = random.randrange(0, 255)
        print(pix)
        time.sleep(0.1)
        cpx.pixels[pix] = (R, G, B)
        count += 1
