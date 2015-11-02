
# Turn On the light when it's become dark.

from gpiozero import LightSensor, LED

sensor = LightSensor(18)
led = LED(16)

sensor.when_dark = led.on
sensor.when_light = led.off

