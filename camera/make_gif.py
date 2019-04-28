from picamera import PiCamera
import datetime as dt
from time import sleep
from os import system

# set up directory, remove all files in it
system('rm -rf gif_images/*')

#init
camera = PiCamera()

# preview viewer, 5 second wait
camera.start_preview()
sleep(5)

# take 30 images
for i in range(30):
    camera.capture('gif_images/image{0:04d}.jpg'.format(i))

# turn off viewer
camera.stop_preview()

#set timestamp str
ts_str = str(dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S"))

#set path to save gif
path_str = '/home/pi/Pictures/gif_{}.gif'.format(ts_str)

# convert gif
system('convert -delay 10 -loop 0 gif_images/image*.jpg {}'.format(path_str))
print('done')
