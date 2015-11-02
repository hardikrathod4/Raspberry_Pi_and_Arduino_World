
# Turn ON the LED when Motion detected...

from gpiozero import MotionSensor, LED

pir = MotionSensor(5)
led = LED(16)

pir.when_motion = led.on
pir.when_no_motion = led.off
