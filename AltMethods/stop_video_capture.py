import signal
import os

def stop_video_capture():
    try:
        # Read the PID from the file
        with open('video_capture_pid.txt', 'r') as file:
            pid = int(file.read())

        # Send a termination signal (SIGINT) to the process
        os.kill(pid, signal.SIGINT)
        print("Termination signal sent.")
    except FileNotFoundError:
        print("PID file not found.")
    except ProcessLookupError:
        print("Process not found.")

# Stop the video capture by sending a termination signal
stop_video_capture()
