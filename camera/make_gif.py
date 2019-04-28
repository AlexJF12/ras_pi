from picamera import PiCamera
import datetime as dt
from os import system

# set up directory, remove all files in it
system('rm -rf gif_images/*')

#init
camera = PiCamera()

for i in range(10):
    camera.capture('gif_images/image{0:04d}.jpg'.format(i))

#set timestamp str
ts_str = str(dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))

#set path to save gif
path_str = '/home/pi/Pictures/gif_{}.gif'.format(ts_str)

# convert gif
system('convert -delay 10 -loop 0 gif_images/image*.jpg {}'.format(path_str))
print('done')
