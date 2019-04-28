# take pic, save with  timestamp

from picamera import PiCamera
import datetime as dt

# init camera
camera = PiCamera()

#set timestamp str
ts_str = str(dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))

#set path to save pic
path_str = '/home/pi/Pictures/pic_{}.jpg'.format(ts_str)

#take pic, save in rasberry_pi directory
camera.capture(path_str)
