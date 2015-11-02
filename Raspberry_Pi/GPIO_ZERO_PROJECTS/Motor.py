
# Run Motor forward and backwards.

from gpiozero import Motor
from time import sleep

# forward: The GPIO pin number the forward gear of the motor is connected to.
# back: The GPIO pin number the reverse gear of the motor is connected to.

motor = Motor(forward=4, back=14)

while True:
    motor.forward()     # Drive the motor forwards.
    sleep(5)
    motor.backward()    # Drive the motor backwards.
    sleep(5)
    
    
