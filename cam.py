import RPi.GPIO as GPIO ################# CROSS CHECK WHAT WORKS ON PI 0 W ###########################################
from picamera import PiCamera
import time

# Setup Var
SEN_PIN = 17 ## USE BCM BOARD NUMBERING (pinout.xyz) Sensor Pin
FPS = 24 ## either 24 or 30 not sure yet
cameraWidth = 1920
cameraHeight = 1080


# Setup 
camera = PiCamera()
camera.framerate = FPS
camera.resolution = (cameraWidth, cameraHeight)



GPIO.setmode(GPIO.BCM)
GPIO.setup(SEN_PIN, GPIO.IN)
# camera.rotation = 180 #would correct for the sensor being sideways. not sure if needed yet. 



def sensor_change(pin):
    lastSenEvent = 0
    if (lastSenEvent - now ) > 0.5: # checks to see if already recording
        
        now = time.time()
        fName = time.strftime("%y-%m-%d %H-%M-%S"+".h264")
        
        camera.start_recording(fName, format='h264')
        lastSenEvent = now # makes it so it woulnt run twice
        print("Recording " + fName)
    else:
        camera.stop_recording()
# Main

GPIO.add_event_detect(SEN_PIN, GPIO.BOTH, sensor_change)

while True:
    time.sleep(1)




