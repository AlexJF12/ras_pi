# take pic, save with  timestamp

from picamera import PiCamera
import datetime as dt

# init camera
camera = PiCamera()

#set timestamp str
ts_str = str(dt.datetime.now().strftime("%Y%m%d-%H%M%S"))

#set path to save pic
path_str = '/home/pi/Pictures/every_five_min/pic_{}.jpg'.format(ts_str)

#take pic, save in rasberry_pi directory
camera.capture(path_str)

# print('pic taken')
