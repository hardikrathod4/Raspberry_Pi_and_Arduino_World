
# run an event every time when button is pressed...!!!!

from gpiozero import Button
from signal import pause

def button_press_event():
              print("Hey, you just pressed a Button...")
              
btn = Button(4)

btn.when_pressed() = button_press_event
pause()
