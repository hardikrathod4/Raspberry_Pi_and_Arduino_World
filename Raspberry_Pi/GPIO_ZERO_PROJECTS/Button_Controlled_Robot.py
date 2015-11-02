
# Use four GPIO buttons as forward/back/left/right controls for a robot

from gpiozero import RyanteckRobot, Button
from signal import pause

robot = RyanteckRobot()

# Define four GPIO buttons

left = Button(26)
right = Button(16)
fw = Button(21)
bw = Button(20)

fw.when_pressed = robot.forward    # Moves frwd until you release the fw button
fw.when_released = robot.stop

left.when_pressed = robot.left     # Turns left until you release the left button
left.when_released = robot.stop

right.when_pressed = robot.right   # Turns right you release the right button
right.when_released = robot.stop

bw.when_pressed = robot.backward   # Moves backwd until you release the bw button
bw.when_released = robot.stop

pause()

