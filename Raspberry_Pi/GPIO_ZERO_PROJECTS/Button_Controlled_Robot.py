
# Use four GPIO buttons as forward/back/left/right controls for a robot

from gpiozero import RyanteckRobot, Button
from signal import pause

robot = RyanteckRobot()

left = Button(26)
right = Button(16)
fw = Button(21)
bw = Button(20)

fw.when_pressed = robot.forward
fw.when_released = robot.stop

left.when_pressed = robot.left
left.when_released = robot.stop

right.when_pressed = robot.right
right.when_released = robot.stop

bw.when_pressed = robot.backward
bw.when_released = robot.stop

pause()

