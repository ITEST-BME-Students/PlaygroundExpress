from adafruit_circuitplayground import cp
import time
import random


# get the time to wait (in milliseconds)
# and convert to seconds
wait_time = random.randint(1000,3000)
wait_time = wait_time / 1000

cp.pixels.fill((255,0,0))
time.sleep(wait_time)
cp.pixels.fill((0,255,0))

duration = 0
while not cp.button_a:
    time.sleep(0.001)
    duration = duration +  0.001
print(duration)
