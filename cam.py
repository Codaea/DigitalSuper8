import picamera
import time
import threading
import sys


class CameraThread(threading.Thread):
    def __init__(self, resolution, framerate):
        super(CameraThread, self).__init__()
        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.is_recording = True

    def run(self):
        video_file = time.strftime("%y-%m-%d %H-%M-%S") + ".h264"  # Specify the file name for the recorded video
        self.camera.start_recording(video_file)
        while self.is_recording:
            self.camera.wait_recording(1)
        self.camera.stop_recording()
        self.camera.close()


def wait_for_enter():
    input("Press Enter to stop recording...")
    camera_thread.is_recording = False


if __name__ == "__main__":
    # Set the desired resolution and framerate
    resolution = (1920, 1080)  # Example resolution: 1280x720
    framerate = 18  # Example framerate: 30 frames per second

    camera_thread = CameraThread(resolution, framerate)
    camera_thread.start()

    wait_for_enter()

    camera_thread.join()
    print("Recording stopped.")