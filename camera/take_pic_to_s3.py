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

print('pic taken')

# upload pic to aws s3

import boto3

s3 = boto3.resource('s3')

# choose which bucket to go to
bucket_raspi = s3.Bucket('raspi-aws')

# choose data, upload a file here
data = open(path_str, 'rb')
bucket_raspi.put_object(Key='pictures/pic_{}.jpg'.format(ts_str), Body=data)

print('uploaded')
