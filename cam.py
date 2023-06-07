import RPi.GPIO as GPIO ################# CROSS CHECK WHAT WORKS ON PI 0 W ###########################################
from picamera import PiCamera

# Setup Var
SEN_PIN = 4 ## USE BCM BOARD NUMBERING (pinout.xyz)
FPS = 24
cameraWidth = 1920
cameraHeight = 1080


# Setup 
camera = PiCamera()
camera.framerate = FPS
camera.resolution = (cameraWidth, cameraHeight)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SEN_PIN, GPIO.IN)


def sensor_change(pin):
    recording = False
    
    if recording(True):
        
 
 
 
 

# camera.rotation = 180 #would correct for the sensor being sideways. not sure if needed yet. 


# Main

GPIO.add_event_detect(SEN_PIN, GPIO.BOTH, sensor_change)




camera.start_recording(format='h264')
camera.stop_recording()



