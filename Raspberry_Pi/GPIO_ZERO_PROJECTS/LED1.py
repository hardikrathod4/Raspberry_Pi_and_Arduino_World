
from gpiozero import LED
from time import sleep

blue = LED(2)

while True:
	blue.on(2)
	sleep(1)
	blue.off(2)
	sleep(1)
