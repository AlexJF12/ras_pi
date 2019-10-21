import datetime as dt
import pathlib
import imageio

# get all filenames
img_files = []

dt = str(dt.datetime.now().strftime("%Y%m%d"))

# define the path
currentDirectory = pathlib.Path('~/Pictures/every_five_min')

for currentFile in currentDirectory.glob(f'*{dt}*'):
    img_files.append(currentFile)

img_files.sort()

# make video
images = []
for filename in img_files:
    images.append(imageio.imread(filename))

imageio.mimsave(f'~/Pictures/daily_vid/{dt}_vid.mp4', images)
