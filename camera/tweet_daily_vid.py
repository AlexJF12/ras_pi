import datetime as dt
from twython import Twython

from twitter_auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# upload a vid

date_for_vid = str((dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y%m%d"))

message = date_for_vid + " in 30 seconds"
video = open('~/Documents/daily_vids/' + date_for_vid + '_vid.mp4', 'rb')

response = twitter.upload_video(media=video, media_type='video/mp4')

twitter.update_status(status=message, media_ids=[response['media_id']])

# print(f'tweeted with media. message: {message}')
