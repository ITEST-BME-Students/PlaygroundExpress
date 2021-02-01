from adafruit_circuitplayground import cp
import time

while True:
    time.sleep(0.1)
    x, y, z = cp.acceleration
    acceleration = (x ** 2 + y ** 2 + z **2) ** 0.5
    print(acceleration)
    if acceleration > 20:
        for i in range(3):
            cp.pixels.fill((255, 0, 0))
            time.sleep(0.25)
            cp.pixels.fill((0, 0, 0))
            time.sleep(0.25)
