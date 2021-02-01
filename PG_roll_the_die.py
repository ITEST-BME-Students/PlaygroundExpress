import time
import board
import neopixel
import random
import digitalio

##############################
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)
##############################

button = digitalio.DigitalInOut(board.BUTTON_B)
# put the button in pull down mode
button.switch_to_input(pull=digitalio.Pull.DOWN)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True: 
    if button.value:
        value = random.randint(0,10)
        print('selected value:', value)
        pixels.fill((0,0,0))
        for i in range(value):
            print(i)
            pixels[i] = wheel((i + 1) * 20)
            time.sleep(0.25)
        time.sleep(1)
