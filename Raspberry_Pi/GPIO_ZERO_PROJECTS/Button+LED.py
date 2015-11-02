# turn on LED when button is pressed...!!!!

from gpiozero import Button
from signal import pause

btn = Button(4)
led = LED(3)

btn.when_pressed() = led.on
btn.when_pressed() = led.off

pause()
