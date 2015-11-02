
# wait for button event before continuing....

from gpiozero import Button

btn = Button(4)

btn.wait_for_press()
print("Button was pressed")
