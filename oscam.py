import argparse
import threading
import picamera
from pythonosc import dispatcher, osc_server

# it would get passed in like 
#   python camera_osc.py --ip 192.168.1.100 --port 9000 --framerate 24 --resolution 1920x1080

# Global variables
recording = False
osc_ip = '127.0.0.1'
osc_port = 5005
frame_rate = 30
resolution = (1280, 720)

def start_recording(camera):
    global recording
    if not recording:
        recording = True
        camera.start_recording('output.h264', format='h264', quality=23, bitrate=2000000)
        print("Recording started.")

def stop_recording(camera):
    global recording
    if recording:
        recording = False
        camera.stop_recording()
        print("Recording stopped.")

def osc_handler(unused_addr, args, start):
    if start:
        start_recording(args[0])
    else:
        stop_recording(args[0])

def run_server(camera):
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/recording", osc_handler, camera)
    server = osc_server.ThreadingOSCUDPServer((osc_ip, osc_port), dispatcher)
    server.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', default='127.0.0.1', help='OSC server IP')
    parser.add_argument('--port', type=int, default=5005, help='OSC server port')
    parser.add_argument('--framerate', type=int, default=30, help='Camera frame rate')
    parser.add_argument('--resolution', type=str, default='1280x720', help='Camera resolution (widthxheight)')
    args = parser.parse_args()

    osc_ip = args.ip
    osc_port = args.port
    frame_rate = args.framerate
    resolution = tuple(map(int, args.resolution.split('x')))

    camera = picamera.PiCamera(resolution=resolution)
    camera.framerate = frame_rate

    # Create a separate thread to run the OSC server
    server_thread = threading.Thread(target=run_server, args=(camera,))
    server_thread.start()

    try:
        while True:
            # Keep the main thread alive
            pass
    except KeyboardInterrupt:
        pass
    finally:
        # Stop recording and clean up resources
        stop_recording(camera)
        camera.close()
        server_thread.join()
