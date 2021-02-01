# Adafruit playground express exercises

For these exercises, feel free to refer to any online documentation you can find. As mentioned in class, this website is a good starting point: [https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express](https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express).

Each exercise comes with an example solution. However, please try to find a solution for yourself before looking at the provided solution.

## Exercise 1:  the right touch

 
 The copper pads labeled A1-A6 on the edge of the PGE can be used as a capacitive touchpad (See image below). For this exercise, program the PGE such that the LED closest to pads A1 and A6 light up if A1 or A6 are touched. The LEDs should be switched off if you let go of the pads. 
 
 **Hints**
 
 You can check whether a given pad is touched using the following code:  ```if cp.touch_A1:``` (replacing  ```A1``` with the label of the appropriate pad). Do not forget to import ```cp``` first using ```from adafruit_circuitplayground import cp```. 

 ![ ](https://cdn-learn.adafruit.com/assets/assets/000/054/810/medium800/circuitpython_cpx_capacitive_touch_pads.jpg?1527982763  "Capacitive pads on the PGE")
 
 You can use the image below to find the indices of the neopixels to use.
 
![](https://cdn-learn.adafruit.com/assets/assets/000/040/971/medium800/circuit_playground_neoorder.jpg?1492800157) 

**Solution: example code can be found here: [https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_light_and_touch.py](https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_light_and_touch.py)**


## Exercise 2:  shake warning

The PGE comes with an accelerometer. This sensor measures how fast the PGE is accelerating. For example, if you shake the device, this sensor will detect the shake.

For this exercise, program the PGE to read out the value of the accelerometer continuously. If the value is larger than a threshold hold value, have all the LEDs on the PGE blink red three times.

**Hints** 

You can read out the sensor as follows,

```
from adafruit_circuitplayground import cp
import time

time.sleep(0.1)
x, y, z = cp.acceleration
acceleration = (x ** 2 + y ** 2 + z **2) ** 0.5
```

This code reads the acceleration in along the ```x```-, ```y```-, and ```z```- direction. Next, it combines these values into a single ```acceleration``` value. The ```time.sleep(0.1)``` gives the sensor some time (0.1 seconds) to measure the acceleration data.

**Solution: example code can be found here: [https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_shake_detection.py]( https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_shake_detection.py)**


## Exercise 3:  making some noise

The PGE has an onboard speaker. You can tell it to play a sound with a specific frequency (pitch) and duration. You can get a feeling (hearing) for what different (pure) frequencies sound like using this applet:

[https://www.szynalski.com/tone-generator/](https://www.szynalski.com/tone-generator/)

For this exercise, extend the previous program such that the PGE also sounds some tones as the LEDs are blinking.

**Hints**

Playing a 500 Hz tone for 1 second is done as follows,

```
from adafruit_circuitplayground import cp 
cp.play_tone(500, 1)
```

**Solution: example code can be found here: [https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_shake_detection_with_sound.py](https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_shake_detection_with_sound.py).**


## Exercise 4:  rolling the die

For this exercise, program the PGE such that it acts as a 10-sided die. Whenever you press the A pushbutton, the PGE generates a number from 1-10. Next, the corresponding number of LEDs are turned on. The LEDs stay on until the button is pressed again.

**Hints**

A random number from 1 to 10 can be generated using the following,

```
import random
value = random.randint(1, 10)
```

You can check whether button A is pressed using this code,

```
if cp.button_a:
```

We have seen a method to switch on a specific number of LEDs in class (if needed, refer to the slides). Remember, the indices of the LEDs go from 0 to 9. The numbers we want to display go from 1-10.

**Solution: example code can be found here: [https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_roll_the_die.py](https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_roll_the_die.py).**
 
## Exercise 5: reaction timer

For this exercise, you will program the PGE as a reaction timer. The PGE will measure how fast a person presses a button after giving the signal to do so. The program should go through the following steps when the run button in Thonny is clicked:

+ Turn all LEDs red (telling the person to hold and wait)
+ Wait a random amount of time (between 1 and 3 seconds)
+ Turn all LEDs green (telling the person to press the button as fast as possible)
+ Measure how long it takes for button A to be pressed
+ Print the duration to the screen


**Hints**

Having the PGE to wait some amount of time can be done using,

```
time.sleep(wait_time)
```

A simple wait to measure time to a button press is the following,

```
duration = 0
while not cp.button_a:
    time.sleep(0.001)
    duration = duration +  0.001
```

**Solution: example code can be found here: [https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_reaction_timer.py](https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_reaction_timer.py).**


## Optional: Glowing

If you have completed the exercise, you can try to upload the following code to the PGE:

[https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_glow.py](https://github.com/ITEST-BME-Students/PlaygroundExpress/blob/main/PG_glow.py)

This code makes the LEDs on the PGE glow. If you shake the PGE, the LEDs will blink faster. If you keep the PGE still, the rate of blinking will gradually decline. Therefore, the LEDs act as a sort of heartbeat that increases you 'excite' the PGE.

You can study and edit the code.
