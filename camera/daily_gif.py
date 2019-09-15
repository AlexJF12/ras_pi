# make 24hr gif from shots

from picamera import PiCamera
import datetime as dt
from time import sleep
from os import system

#set timestamp strs
ts_str = str(dt.datetime.now().strftime("%Y%m%d-%H"))
day = str(dt.datetime.now().strftime("%Y%m%d"))
hour = str(dt.datetime.now().strftime("%H"))

# make folder for today
system("mkdir {}".format(day))

#set path to save pic
path_str = '/home/pi/Pictures/daily/{}/pic_{}.jpg'.format(day, ts_str)

# init camera
camera = PiCamera()

#take pic, save in rasberry_pi directory
camera.capture(path_str)
print('pic taken')


def make_gif():
    #set path to save gif
    path_str = '/home/pi/Pictures/gif_{}.gif'.format(ts_str)

    # convert gif, status update
    system('convert -delay 10 -loop 0 gif_images/image*.jpg {}'.format(path_str))
    print('done')

if hour = '00':
    make_gif()
