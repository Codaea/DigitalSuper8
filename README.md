# Digital Super 8 Tutorial/Guide


## About 
Guide was converted from google docs. original link [Here](https://docs.google.com/document/d/1fJHuiId_inuBiVWZYaGCTwVPXUBCfjpttEX59x5DVYc/edit?usp=sharing)

Contact me - [dakotajayroth@gmail.com](mailto:dakotajayroth@gmail.com) , codaea on discord

[The Trello Board, For things I need to do](https://trello.com/b/N0vrLmnk/digital-super-8)

This project was inspired by [befinitiv](https://gist.github.com/befinitiv), [NoLab & Hayes Urban](https://www.digitaltrends.com/photography/nolab-digital-film-cartridge-turns-old-super-8-camera-modern-day-moviemaker/), and [Patrick Steemers](https://www.digitalsuper8.com/digital-super-8-our-story/)

Tutorials that where refrenced are linked in their respective sections

Pretty Much all Co-written by ChatGPT

Note: I find it hard to balance the amount of support I give in the guide so feel free to skip sections you don’t need or already know. The reason it's as in depth as it is is because this was the resource I wish I had when building my own. 

Anything in yellow is meant to be changed at some point too.


## Specs -

1920x1080p@18fps

52 Hour Battery Life

Old Timey Feel


## Pictures -

|                                                                                                                                                                                                |                                                                                                                                                                                                |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](https://lh4.googleusercontent.com/N9WStgUpafsRkpSavhaYxvbfB3vMQ1aVpAseX_1Lv_LKRPiE2hMUqeU6u_ddUxEcWklwK4z9pVK5pTfS7cwS7QKglvorHLBtAPrZyestRgZzLdzsl1yYWhTwYdlsk_D-2jBcBke_FL4uTY9zg8vl2fg) | ![](https://lh3.googleusercontent.com/Ryk4h8kusf8vvPDvAYRlPZZL71cM5oikyUnTYZUTa61jUqe0G2hrKttjIFy_YONp95157CxwENz-bRif5ZgHcDU6tSRhNRgzn_7UXKakUogmTu6TIfI6fKkO4a0DyfEK-_9V_w3mdQ8jK6gPpfR7qhc) |
| ![](https://lh4.googleusercontent.com/48TRNcJfMg1ylxVkr3t80OarTxgdiDukDIJXDrx8F06XQ6t1YqJ8quWexktKOqvRgE5IW60faBQc8y_CsvNbGiR4smz63cf16lCAaQfZBClsHJWp_HZKBhvkK85vbl-JnV0NYf2Tu8s5FD_8R1whuGQ) | ![](https://lh6.googleusercontent.com/AJBbRa-g0EhmjsclDEl3zmaPVHfc7Z2ChL3DJVYLyLmOeRfHevYiJavTghsXQdIKz7RHD50OTNjDD2eYe9XKACOTd57yUjAuva0EAQacXHrRI57D9h4EFDb2oAzWlFXeYjM2khSR6sAsg2Km4dW8jog) |

V1 Photos


##  READ ME!! CURRENT PROBLEMS!! READ ME!! 

This entire tutorial is super unpolished. Its gonna get fixed eventually, but for now, some of the instructions may be wrong.

Hardware Problems:

- Currently I am having trouble staying in focus throughout the whole zoom range along with never being able to get in focus when zoomed all the way out and in. The placement of the sensor at the moment consists of Jamming it as close to the film gate as I can so hopefully I can pull it together and fix that soon.

Software Problems:

- I was having trouble with the autocam.py being CPU intensive so the short term solution was to just make it accessible via ssh where one script started recording in background and the second stopped recording. Will leave files for that probably on a separate branch or folder. (MOSTLY SOLVED, can be shortened to me being a dumbass on read write operations.)


# The Hardware


## Parts Used With Links 

- [Raspberry Pi 0 W](https://www.pishop.us/product/raspberry-pi-zero-w/?src=raspberrypi)
- MicroSD Card
- [Adafruit PowerBoost 500 Charger](https://www.adafruit.com/product/1944)
- [22 Gauge Wire (Insulated)](https://www.amazon.com/Gauge-Wire-Solid-Hookup-Wires/dp/B088KQFHV7/ref=sr_1_1_sspa?keywords=22+gauge+wire&qid=1687082198&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
- [Raspberry Pi 0 Spy Cam](https://www.amazon.com/dp/B07T948TF3/ref=twister_B09TW7PM6H?_encoding=UTF8&th=1)
- [M2.5 Hex Nuts](https://www.amazon.com/HELIFOUNER-Pieces-Stainless-Steel-Screws/dp/B0B6474KGM/ref=sr_1_4?crid=3537SOL2J4YQV&keywords=m2.5+Hex+Nuts&qid=1687082456&sprefix=m2.5+hex+nuts%2Caps%2C169&sr=8-4)
- M2.5\*5 Screws
- Super Glue
- [Breadboard Friendly SPDT switch](https://www.adafruit.com/product/805)
- Double Sided Tape/Double Sided Sticky Pads
- 3D Printed Cartridge
- [Wire Connectors](https://www.amazon.com/Pluggable-Connectors-Universal-Terminals-Wire-Stripping/dp/B07PRZMYD4/ref=sr_1_3?keywords=quick+connect+22+awg&qid=1687082783&sr=8-3) (If you want to make it through TSA)
- [18650 battery](https://www.amazon.com/CBJJ-Rechargeable-Flashlight-Headlamps-U-S-Shipping/dp/B0BZYPF7HZ/ref=sr_1_13?crid=1F9XTMMS7ODEP&keywords=18650+battery&qid=1687082873&sprefix=18650+batte%2Caps%2C191&sr=8-13)

**Note**: These are all the parts I used, in reality, you really only need the Pi 0 w, the powerboost , battery , a SPDT switch and the pi 0 camera.


## 3D Printed Parts

You can get the 3D files **here**

These are the settings that i used on my Ender 3 v2

- .2mm layer height
- 200C Hotend 50C bed
- Tree supports

Default should hopefully work fine. Just make sure to use tree supports as they are easier to remove.


## Gluing In Hex Nuts

This one is a little self explaining but here it goes. 

I used super glue and just dabbed a little on the bottom and used pliers to drop them in. I tried using a screw a little screwed in to help position it but I was just afraid that it might glue the screw in. 

**The PowerBoosts on bottom hex nuts are NOT flush!!**

**IMAGE HERE**


## Wiring And Diagram

![](https://lh5.googleusercontent.com/So7JXKJIPgKPiOMEBY7GBiRvX3NWsmQn7LObn4TVXnfLwnnzo8aiVmH3M_GHBBDOyb1utDiBMRyltqz23-QxDGvKdaEKI6VDvgcEGtAl1qkuBcoD7ngIIZ6EULjt0f_BV8i1YjQLB5LjzLSg8vLWOlA)

It doesn't really matter what ground or 5v you use on the pi, I just picked these randomly.

I recommend leaving the Leads between the pi along with the switch a little bit longer even if they go Directly Next to each other inside the cartridge. Makes screwing things in easier.

Connections:

- Adafruit 5v to raspberry pi 5v
- Adafruit ground to raspberry pi ground
- EN pin and ground connected via SPDT switch
- Ground and batt connected to battery


## Soldering to a battery - (if you want to)

I used [this video](https://www.youtube.com/watch?v=Zx7d5yJdWp0) but you could always use [one of these](https://www.amazon.com/HiLetgo-10pcs-Battery-Holder-Storage/dp/B00LSG5BKO/ref=asc_df_B00LSG5BKO/?tag=hyprod-20&linkCode=df0&hvadid=241941495556&hvpos=&hvnetw=g&hvrand=10181915753709795318&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9033045&hvtargid=pla-438278133726&psc=1). At the moment I haven't found a way to make it fit in the cartridge but if you can that's great.


## Removing The Lens From 0 Spy Cam

I used a pair of needle nose pliers to twist out the lens itself. It just unscrews. For the square lookin casing part I used the pliers to squeeze it horizontally to break the glue bonds. You could also use a clamp for breaking the glue bonds. Just make sure that it isn't squeezing on the circuit board. I'm using a old sensor thats broken as a example for this, so there is a little more wear.


## ![](https://lh6.googleusercontent.com/-nMV27ApkgHhsyvWpHyrbQG0xrsItpQouRz2R5_wCZgAiKloI8hsYdz-drsaDN-9gbqrr0jslw3dLf-iyHw5iK3eBPIjJSh8UQ4EJjrzPVsRHgJLeNIQjSP850DQCXQm4ByhceysH_9AbpYOUTttje0)

A little Diagram to help out

![](https://lh3.googleusercontent.com/GwDpP_8cBCrh5gFgmqgvMGZ5lrf8_Gp3hsIR43ijjOmJYyrITgAC3E0tZzj8lVKlDOnt8RPgLlNo9pAuRiFX1fxeeihxbbjLvITOuqbNLiuYn1EPxnP5w4ZnbwNdy2XKMjd1YAIPmFh86hjvjEAaAyk)

Unscrewing the lens part


## ![](https://lh4.googleusercontent.com/OgTbZcRJBsmijkFeCKsQgfHKfPryyzieEYvcUa-RwUqHPzwT8MXAqYWU7SzuKL4thdh72SEBd_NoRYQeWhOrJQUIl2_ik26dtNMXhosDf4N4drue3ANaOD0Q44eJ5YJA15INdfrVgwJUVxX2ZDjc5po)

Lens part unscrewed


## ![](https://lh6.googleusercontent.com/B34fXAguH0bEESuqGY98T6rm3j7mTgKInNzIrccn68-RKpZnmzn0d0iiDEIJXPqfzRH-69cJhd04tIYnqeetWc1MmyQgCrZF7KXESLIWfY1E_tflW3drkel8_aV3_tNWVg9g5ARnQ9rXqJb-MhR9TcY)

Breaking glue bond


## ![](https://lh5.googleusercontent.com/sTOicx-gT--Bf_D8mW-5HtLr7vL6Xl8gb2Uv8ACuqqKyTRDdCw_XoiIsaFGIrRd-7KUndQZf0ve5mEKF1v5IMZ7Ww2PWgR3QmwinHCnKEnr6KklC3AcjLqYTEMPW52mAVBVVUqlKWx8VX-00oGR_IM0)

All Done!


## Connecting the Camera To the Raspberry pi

- Locate the Camera Module port
- Gently pull up on the edges of the port’s plastic clip
- Insert the Camera Module ribbon cable; make sure the connectors at the bottom of the ribbon cable are facing the contacts in the port.
- Push the plastic clip back into place

![](https://lh6.googleusercontent.com/fFR9tSKyyXDHWOqcaclYvbFzd-rWlDeM6n1pGexW9H7MGxF8569AEA1nV0BZhr1iRGmZUSRdovrKbjMOYrZnCa4Q-bVi4l-xu7oca8toah-OuLVHgF7BTO3lBLqPdyvFTCX0OkQjhpAS3ZSN5RD0M1M)

- To enable Camera Module Run sudo raspi-config in terminal 
- Select Interfacing options and press Return. Use the Arrow Keys to Navigate
- Select Pi Camera
- Select Yes
- Select Finish
- Select Yes for reboot

To test, run Raspistill –o image.jpg and if no errors and the red light on the ribbon cable turns on, you're good!

[Image Src](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2)

[Another Tutorial](https://techoverflow.net/2019/07/23/how-to-enable-raspberry-pi-camera-using-raspi-config/)


## Gluing the Sensor in

I Spent a bit of time getting perfect alignment with the sensor so i recommend you glue it in as close as flush as possible with the least amount of space between the sensor back and the glue. Make sure that the sensor is centered below the hole above it. I found that the camera's film gate tends to push it into the right spot so maybe slide it in while the glue is setting.


# The Software


## Imaging Raspberry pi


## Enabling Legacy Camera (If Not Already)

If you haven't done this it's up in the Connecting the Camera To Raspberry pi section but here it is again.

- To enable Camera Module Run sudo raspi-config in terminal 
- Select Interfacing options and press Return. Use the Arrow Keys to Navigate
- Select Pi Camera
- Select Yes
- Select Finish
- Select Yes for reboot

To test, run Raspistill –o image.jpg


## Creating a file sharing server and setting up permissions (Samba)


## Downloading Code to Raspberry Pi
1. sudo apt install git
2. git clone 


## Finding Darkness Threshold For Your Super 8


## Running Code At Startup

1. Run sudo crontab -e in terminal
2. Choose nano (1)
3. @reboot Your command here & 

\- use full path and run as admin so sudo python /home/pi/autocam.py &

[Video Tutorial](https://www.youtube.com/watch?v=Gl9HS7-H0mI)


# Closing Thoughts
