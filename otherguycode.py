#!/usr/bin/python

import glob
import socket
import time
from threading import Timer
import picamera
import RPi.GPIO as GPIO



SENSOR_PIN = 18
W = 1296
H = 972
FPS = 18

IP = '192.168.0.21'
PORT = 5000


def start_recording():
	global camera_data
	global camera
	camera_data = CameraData()
	camera.start_recording(camera_data, format='h264')
	print('start')

def stop_recording():
	global camera_data
	global camera
	camera.stop_recording()
	camera_data.stop()
	print('stop')


def timer_stop():
	global stop_timer_running
	stop_timer_running = False
	stop_recording()

last_sensor_event = 0
stop_timer_running = False

def sensor_change(pin):
	global last_sensor_event
	global stop_timer
	global stop_timer_running

	now = time.time()

	if abs(last_sensor_event - now) > 0.5:
		start_recording()

	last_sensor_event = now

	if stop_timer_running:
		stop_timer.cancel()

	stop_timer = Timer(0.5, timer_stop)
	stop_timer.start()
	stop_timer_running = True


GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(SENSOR_PIN, GPIO.BOTH, sensor_change)


# This class writes data to file and streams it in parallel
class CameraData(object):
	def __init__(self):
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.client_socket.connect((IP, PORT))
		self.connection = self.client_socket.makefile('wb')
		self.file = open(self.create_unique_file_name(), 'wb')

	def create_unique_file_name(self):
		return '%d.h264' % len(glob.glob('*'))

	def write(self, s):
		self.connection.write(s)
		self.file.write(s)

	def flush(self):
		pass

	def stop(self):
		self.connection.close()
		self.client_socket.close()
		self.file.close()


# Make a file-like object out of the connection
try:
	camera = picamera.PiCamera()
	camera.resolution = (W, H)
	camera.framerate = FPS

	while True:
		time.sleep(1)
	#camera.wait_recording(60)
finally:
	pass