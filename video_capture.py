import time
import picamera
import signal
import os

# Configuration
fps = 18  # Frames per second 19 is magic number according to someone one the internet. FOR DAYLIGHT???
resolution = (1920, 1080)  # Resolution (width, height)
filename = time.strftime("%y-%m-%d %H-%M-%S") + ".h264"  # Default filename

def start_video_capture():
    camera = picamera.PiCamera()
    camera.resolution = resolution
    camera.framerate = fps
    camera.start_recording(filename)
    return camera

def stop_video_capture(camera):
    camera.stop_recording()
    camera.close()

def handle_termination(signal, frame):
    stop_video_capture(camera)
    print("Video capture stopped.")
    exit(0)

def write_pid_to_file(pid):
    with open('video_capture_pid.txt', 'w') as file:
        file.write(str(pid))

# Start video capture
camera = start_video_capture()
print("Video capture started.")

# Write the PID to a file
write_pid_to_file(os.getpid())

# Register the termination signal handler
signal.signal(signal.SIGINT, handle_termination)
signal.signal(signal.SIGTERM, handle_termination)

# Keep the script running indefinitely
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

handle_termination(None, None)
