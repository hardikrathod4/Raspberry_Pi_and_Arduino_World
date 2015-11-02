
from gpiozero import LED
from signal import pause

red = LED(2)

red.blink()
pause()
