# pic_ffmpeg_to_vid.py

# command line to convert yesterdays pics to vid

import datetime as dt
import os

date_for_vid = str((dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y%m%d"))

command_line_code = "ffmpeg -framerate 10 -f image2 -pattern_type glob -i 'pic_" + date_for_vid + "-*.jpg' ~/daily_vids/" + date_for_vid + "}.mp4"

os.system(command_line_code)
