import picamera
import time
from PIL import Image

def calculate_average_pixel_value(image):
    # Convert the image to grayscale for simplicity
    grayscale_image = image.convert('L')
    
    # Calculate the average pixel value
    pixels = grayscale_image.getdata()
    total_value = sum(pixels)
    num_pixels = len(pixels)
    average_value = total_value // num_pixels
    
    return average_value

def is_dark(pixel_value):
    # Check if the pixel value is considered dark based on your criteria
    # You can adjust the threshold values as per your requirement
    darkness_threshold = 50  # Adjust this value as needed
    return pixel_value < darkness_threshold

def find_val():
    with picamera.PiCamera() as camera:
        camera.resolution = (1920, 1080)
        camera.framerate = 5
        camera.start_preview()
        time.sleep(2)  # Wait for the camera to adjust to the light conditions
        
        while True:
            camera.capture('image.jpg', use_video_port=True)  # Capture a frame
            # Open the captured image using PIL
            image = Image.open('image.jpg')
            # Calculate the average pixel value
            pixel_value = calculate_average_pixel_value(image)
            # Print Value to console
            result = f"{pixel_value} SO.. {is_dark(pixel_value)}"
            print(result)
            time.sleep(1)

find_val()