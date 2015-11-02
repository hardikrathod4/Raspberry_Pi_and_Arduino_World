
# Making different colours with RGB led.

from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=9, green=10, blue=11)

led.red = 1  # full red
led.red = 0.5  # half red

led.rgb = (0, 1, 0)  # full green

led.rgb = (1, 0, 1)  # magenta
led.rgb = (1, 1, 0)  # yellow
led.rgb = (0, 1, 1)  # cyan
led.rgb = (1, 1, 1)  # white

led.rgb = (0, 0, 0)  # off

# slowly increase intensity of blue
for n in range(100):
    led.blue += 0.01
    sleep(0.1)
    
    
