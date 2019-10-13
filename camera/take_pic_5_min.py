# take pic, save to every_five_min

import picamera
# from picamera import Color
import datetime as dt
import time

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(3)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g

    camera.annotate_text_size = 24
    # camera.annotate_foreground = picamera.Color('black')
    # camera.annotate_background = picamera.Color('white')
    camera.annotate_text = str(dt.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))

    #set timestamp str
    ts_str = str(dt.datetime.now().strftime("%Y%m%d-%H%M%S"))

    #set path to save pic
    path_str = '/home/pi/Pictures/every_five_min/pic_{}.jpg'.format(ts_str)

    # take pic
    camera.capture(path_str)

    # print filename
    print(path_str)
