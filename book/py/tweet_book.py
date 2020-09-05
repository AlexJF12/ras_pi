import pandas as pd

import json

# for twitter
from twython import Twython

with open('../auth/twitter_access_keys.json') as json_file:
    twitter_keys = json.load(json_file)

# auth
twitter = Twython(
    twitter_keys['consumer_key'],
    twitter_keys['consumer_secret'],
    twitter_keys['access_token'],
    twitter_keys['access_token_secret']
)

# book df
df = pd.read_csv('~/Documents/dev/book/old_man_and_the_sea_timestamps.csv')

# get next paragraph to tweet
df_nontweeted = (
    df[df['tweeted_timestamp'].isnull()]
    .sort_values(by=['p_num', 'chunk_num'])
    )

next_p_to_tweet = df_nontweeted['p_num'].min()

list_of_tweet_text = df_nontweeted[df_nontweeted['p_num'] == next_p_to_tweet]['text_to_tweet'].to_list()

# tweet out each chunk in paragraph
for text in list_of_tweet_text:
    print(text)
    print(next_p_to_tweet)
    twitter.update_status(status=text)

# save timestamp of when tweet was sent and save new csv
df.loc[df.p_num == next_p_to_tweet, "tweeted_timestamp"] = pd.Timestamp.now()
df.to_csv('~/Documents/dev/book/old_man_and_the_sea_timestamps.csv')