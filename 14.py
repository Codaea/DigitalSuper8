import RPi.GPIO as GPIO
import time

Sen_Pin = 6

is_recording = False

GPIO.setmode(GPIO.BCM)
# Set GPIO pin 6 as input
GPIO.setup(Sen_Pin, GPIO.IN)

# Function to start recording
def start_recording():
    global is_recording
    if not is_recording:
        is_recording = True
        print("Recording started.")

# Function to stop recording
def stop_recording():
    global is_recording
    if is_recording:
        is_recording = False
        print("Recording stopped.")

# Main program loop
while True:
    # Read the state of the switch
    switch_state = GPIO.input(Sen_Pin)

    # If the switch is enabled (ON) and not already recording, start recording
    if switch_state == GPIO.HIGH:
        start_recording()

    # If the switch is disabled (OFF) and currently recording, stop recording
    if switch_state == GPIO.LOW:
        stop_recording()