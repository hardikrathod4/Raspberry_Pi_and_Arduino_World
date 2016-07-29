import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
buttonPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

while True:
    #assuming the script to call is long enough we can ignore bouncing
    if (GPIO.input(buttonPin)):
        #this is the script that will be called (as root)
        os.system("fswebcam -r 960x720 -d /dev/video0 /home/pi/RPi/Webcam_Security_System/images/webcam.jpg")
        os.system("python /home/pi/RPi/Webcam_Security_System/send_gmail.py")
