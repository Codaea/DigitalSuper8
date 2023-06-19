## Digital Super 8

Guide Moved To Docs for now <br>
https://docs.google.com/document/d/1fJHuiId_inuBiVWZYaGCTwVPXUBCfjpttEX59x5DVYc/edit?usp=sharing

##Docs To Markdown Coversion (IMAGES MAY BE BROKEN)

<!-----

You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 6

Conversion time: 3.191 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Mon Jun 19 2023 01:55:19 GMT-0700 (PDT)
* Source doc: How to make a digital Super 8
* Tables are currently converted to HTML tables.
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 0; ALERTS: 6.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>
<a href="#gdcalert2">alert2</a>
<a href="#gdcalert3">alert3</a>
<a href="#gdcalert4">alert4</a>
<a href="#gdcalert5">alert5</a>
<a href="#gdcalert6">alert6</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



## Digital Super 8


### About 

Contact me - [dakotajayroth@gmail.com](mailto:dakotajayroth@gmail.com) , codaea on discord

This project was inspired by [befinitiv](https://gist.github.com/befinitiv), [NoLab & Hayes Urban](https://www.digitaltrends.com/photography/nolab-digital-film-cartridge-turns-old-super-8-camera-modern-day-moviemaker/), and [Patrick Steemers](https://www.digitalsuper8.com/digital-super-8-our-story/)

Tutorials that where refrenced are linked in their respective sections

Pretty Much all Co-written by ChatGPT

Note: I find it hard to balance the amount of support I give in the guide so feel free to skip sections you don’t need or already know. The reason it's as in depth as it is is because this was the resource I wish I had when building my own. 

Anything in yellow is meant to be changed at some point too.


### Specs -

1920x1080p@18fps

152 Hour Battery Life (Not sure if this is right?)

Fun Fact! Will probably get your bag searched at TSA! (it happened to me)


### Pictures -


<table>
  <tr>
   <td>
<h2>

<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image1.jpg" width="" alt="alt_text" title="image_tooltip">
</h2>


   </td>
   <td>
<h2>

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image2.jpg" width="" alt="alt_text" title="image_tooltip">
</h2>


   </td>
  </tr>
  <tr>
   <td>
<h2>

<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image3.jpg" width="" alt="alt_text" title="image_tooltip">
</h2>


   </td>
   <td>
<h2>

<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


<img src="images/image4.jpg" width="" alt="alt_text" title="image_tooltip">
</h2>


   </td>
  </tr>
</table>



### ** READ ME!! CURRENT PROBLEMS!! READ ME!! **

Hardware Problems:



* Currently I am having trouble staying in focus throughout the whole zoom range along with never being able to get in focus when zoomed all the way out and in. The placement of the sensor at the moment consists of Jamming it as close to the film gate as I can so hopefully I can pull it together and fix that soon.

Software Problems:



* I was having trouble with the autocam.py being CPU intensive so the short term solution was to just make it accessible via ssh where one script started recording in background and the second stopped recording. Will leave files for that probably on a separate branch or folder.


### Alternative Recording Control

There are lots of different ways to start and stop recording but some are more robust than others. Here is a list of all the ways I could think of and could find.

Internal 



* Photo Sensor On Film Spinny Thing With LED other side
* Mechanical Switch attached to SpinnyThing
* Magnetic Switch attached to SpinnyThing
* Image Sensor Light Levels
* Sound

External



* OSC (Open Sound Control)
* Website
* SSH


## The Hardware


### Parts Used With Links 



* [Raspberry Pi 0 W](https://www.pishop.us/product/raspberry-pi-zero-w/?src=raspberrypi)
* MicroSD Card
* [Adafruit PowerBoost 500 Charger](https://www.adafruit.com/product/1944)
* [22 Gauge Wire (Insulated)](https://www.amazon.com/Gauge-Wire-Solid-Hookup-Wires/dp/B088KQFHV7/ref=sr_1_1_sspa?keywords=22+gauge+wire&qid=1687082198&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1)
* [Raspberry Pi 0 Spy Cam](https://www.amazon.com/dp/B07T948TF3/ref=twister_B09TW7PM6H?_encoding=UTF8&th=1)
* [M2.5 Hex Nuts](https://www.amazon.com/HELIFOUNER-Pieces-Stainless-Steel-Screws/dp/B0B6474KGM/ref=sr_1_4?crid=3537SOL2J4YQV&keywords=m2.5+Hex+Nuts&qid=1687082456&sprefix=m2.5+hex+nuts%2Caps%2C169&sr=8-4)
* M2.5*5 Screws
* Super Glue
* [Breadboard Friendly SPDT switch](https://www.adafruit.com/product/805)
* Double Sided Tape/Double Sided Sticky Pads
* 3D Printed Cartridge
* [Wire Connectors](https://www.amazon.com/Pluggable-Connectors-Universal-Terminals-Wire-Stripping/dp/B07PRZMYD4/ref=sr_1_3?keywords=quick+connect+22+awg&qid=1687082783&sr=8-3) (If you want to make it through TSA
* [18650 battery](https://www.amazon.com/CBJJ-Rechargeable-Flashlight-Headlamps-U-S-Shipping/dp/B0BZYPF7HZ/ref=sr_1_13?crid=1F9XTMMS7ODEP&keywords=18650+battery&qid=1687082873&sprefix=18650+batte%2Caps%2C191&sr=8-13)

**Note**: These are all the parts I used, in reality, you really only need the Pi 0 w, the powerboost , battery , a SPDT switch and the pi 0 camera.


### Wiring Diagram



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")



### Removing The Lens From 0 Spy Cam

I used a pair of needle nose pliers to twist out the lens itself. It just unscrews. For the square lookin casing part I used the pliers to squeeze it horizontally to break the glue bonds. I Plan on making a video in the future. 

IMAGES HERE


### Connecting the Camera To the Raspberry pi



* Locate the Camera Module port
* Gently pull up on the edges of the port’s plastic clip
* Insert the Camera Module ribbon cable; make sure the connectors at the bottom of the ribbon cable are facing the contacts in the port.
* Push the plastic clip back into place



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.gif). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.gif "image_tooltip")




* To enable Camera Module Run sudo raspi-config in terminal 
* Select Interfacing options and press Return. Use the Arrow Keys to Navigate
* Select Pi Camera
* Select Yes
* Select Finish
* Select Yes for reboot

To test, run Raspistill –o image.jpg and if no errors and the red light on the ribbon cable turns on, you're good!

[Image Src](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/2)

[Another Tutorial](https://techoverflow.net/2019/07/23/how-to-enable-raspberry-pi-camera-using-raspi-config/)


## The Software


### Imaging Raspberry pi


### Enabling Legacy Camera (If Not Already)

If you haven't done this it's up in the Connecting the Camera To Raspberry pi section but here it is again.



* To enable Camera Module Run sudo raspi-config in terminal 
* Select Interfacing options and press Return. Use the Arrow Keys to Navigate
* Select Pi Camera
* Select Yes
* Select Finish
* Select Yes for reboot

To test, run Raspistill –o image.jpg


### Creating a file sharing server (Mamba)
