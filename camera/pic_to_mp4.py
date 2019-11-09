import datetime as dt
import pathlib
import imageio


def pic_to_mp4(dt):
    """
    grab all of yesterday's pictures and converts it to a mp4
    """

    # default to yesterday
    # dt = str((dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y%m%d"))

    # define the path
    currentDirectory = pathlib.Path('~/Pictures/every_five_min')

    # get all filenames
    img_files = []

    for currentFile in currentDirectory.glob('*' + dt + '*'):
        img_files.append(currentFile)

    img_files.sort()

    # make video
    images = []
    for filename in img_files:
        images.append(imageio.imread(filename))

    imageio.mimsave('~/Pictures/daily_vid/' + 'dt' + '_vid.mp4', images)

pic_to_mp4(dt = str((dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y%m%d")))
