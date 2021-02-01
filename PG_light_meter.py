# Circuit Playground Light Sensor
# Reads the on-board light sensor and graphs the brightness with NeoPixels

import time
import board
import neopixel
import analogio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.show()

light = analogio.AnalogIn(board.LIGHT)

# assume range from 1000-15000
min_val = 1000
max_val = 10000

pixels.fill((0,0,0))

while True:
    # light value remapped to pixel position
    value = light.value
    print(value)
    if value < min_val: value = min_val
    if value > max_val: value = max_val
    value = value - min_val
    value = value/(max_val-min_val)
    value = round(value * 9)
    
    print(value)

    for i in range(2, 10):
        if i < value: pixels[i] = (10,10,10)
        if i > value: pixels[i] = (0,0,0)

    pixels.show()
    time.sleep(0.25)
