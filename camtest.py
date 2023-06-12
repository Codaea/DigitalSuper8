import RPi.GPIO as GPIO ################# CROSS CHECK WHAT WORKS ON PI 0 W ###########################################
from picamera import PiCamera
import time

FPS = 24
cameraWidth = 1920
cameraHeight = 1080
fName = time.strftime("%y-%m-%d %H-%M-%S"+".h264")

camera = PiCamera()
camera.framerate = FPS
camera.resolution = (cameraWidth, cameraHeight)



camera.start_recording(fName, format='h264')
print("recording!")
time.sleep(15)
camera.stop_recording()
print("stopped!")