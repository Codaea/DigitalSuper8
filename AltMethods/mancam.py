import RPi.GPIO as GPIO
from picamera import PiCamera
import time

# Setup Var
Sen_Pin = 6 ## USE BCM BOARD NUMBERING (pinout.xyz) Sensor Pin


FPS = 24 ## either 24 or 30 not sure yet
cameraWidth = 1920
cameraHeight = 1080

is_recording = False
last_record = 0
# Setup 
camera = PiCamera()
camera.framerate = FPS
camera.resolution = (cameraWidth, cameraHeight)

GPIO.setmode(GPIO.BCM)
# Set GPIO pin 6 as input
GPIO.setup(Sen_Pin, GPIO.IN)

# Function to start recording
def start_recording():
    global is_recording
    if not is_recording:
        if (last_record - now) > 1:
            is_recording = True
        
            fName = time.strftime("%y-%m-%d %H-%M-%S"+".h264")
            camera.start_recording(fName, format='h264')
            print("Recording started.")

# Function to stop recording
def stop_recording():
    global is_recording
    global last_record
    if is_recording:
        is_recording = False
        camera.stop_recording()
        print("Recording stopped.")
        
        last_record = now

# Main program loop
while True:
    # Read the state of the switch
    switch_state = GPIO.input(Sen_Pin)
    # Updates Time to Now
    now = time.time()
    # If the switch is enabled (ON) and not already recording, start recording
    if switch_state == GPIO.HIGH:
        start_recording()

    # If the switch is disabled (OFF) and currently recording, stop recording
    if switch_state == GPIO.LOW:
        stop_recording()