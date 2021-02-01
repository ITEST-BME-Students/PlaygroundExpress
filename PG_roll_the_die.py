from adafruit_circuitplayground import cp
import time
import random


while True:
    if cp.button_a:
        while cp.button_a: time.sleep(0.1) # optional, results in cleaner detection of button press
        cp.pixels.fill((0, 0, 0))
        value = random.randint(1, 10)
        print(value)
        for i in range(value):
            cp.pixels[i] = ((255, 0 , 0))
        
