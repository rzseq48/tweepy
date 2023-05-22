import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "1395774269339041794-ySPM7G4zo4yGSpMlXlGL8ugoIehutJ"
access_secret = "JdJqtQyWJl7JpAni7ddfTcEgUaZohEmQt2dD5I2zqntiG"
consumer_key = "7qFxTXnfxvjEWbsg5xg86QqJP"
consumer_secret = "DKlBic6VbT0PJAqj4dhz6Wxbl1sXbbcWCrr2KJpjNNU3pKjSkT"

#twitter authentication

auth = tweepy.OAuthHandler(access_key,access_secret)
auth.set_access_token(consumer_key,consumer_secret)

#creating an API object

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = '@elonmusk',
                           count = 200,
                           #200 us the max allowed count
                           include_rts = False, #if you want to include retweets
                           tweet_mode = 'extended'
                           )

print(tweets)


