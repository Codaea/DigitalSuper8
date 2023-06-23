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
    darkness_threshold = 250  # Adjust this value as needed
    if darkness_threshold == 250:
        print("Darkness Threshold is 250. Did you set the value?") # Reminds user to set darkness_threshold
        pass 
    return pixel_value < darkness_threshold

def record_when_light():
    fps = 18  # Adjust the desired frames per second
    resolution = (1920, 1080)  # Adjust the desired resolution
    
    with picamera.PiCamera() as camera:
        camera.resolution = resolution
        camera.framerate = fps
        camera.start_preview()
        time.sleep(2)  # Wait for the camera to adjust to the light conditions
        
        recording = False
        
        while True:
            camera.capture('image.jpg', use_video_port=True)  # Capture a frame
            
            # Open the captured image using PIL
            image = Image.open('image.jpg')
            
            # Calculate the average pixel value
            pixel_value = calculate_average_pixel_value(image)
            
            if is_dark(pixel_value):
                # If it's dark, stop recording if it's currently recording
                if camera.recording:
                    camera.stop_recording()
                    print("Stopped Recording.")
            else:
                # If it's light, start recording if it's not currently recording
                if not camera.recording:
                    video_file = time.strftime("%y-%m-%d %H-%M-%S") + ".h264"  # Specify the file name for the recorded video
                    camera.start_recording(video_file)
                    print("Started Recording.")
            
            time.sleep(2)  # Wait for 1 second before capturing the next frame
time.sleep(180) #waits for pi to load up for launching on boot
record_when_light()