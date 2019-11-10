# pic_ffmpeg_to_vid.py

# command line to convert yesterdays pics to vid

import datetime as dt
import os

date_for_vid = str((dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y%m%d"))

# ffmpeg -framerate 10 -f image2 -pattern_type glob -i 'pic_20191108-*.jpg' ~/Documents/test.mp4

# 12 frames per second
# glob search for files with date 

command_line_code = "cd ~/Pictures/every_five_min ; ffmpeg -framerate 12 -f image2 -pattern_type glob -i 'pic_" + date_for_vid + "-*.jpg' ~/Documents/daily_vids/" + date_for_vid + "_vid.mp4"

print(command_line_code)

os.system(command_line_code)
