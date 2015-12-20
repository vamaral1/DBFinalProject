import MySQLdb as db
import re
import time
import datetime

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import tweepy
import json

#Variables that contains the user credentials to access Twitter API 
access_token = "2714753071-RMkfVbxgUKowUwW0xUYAk8cVpQDFKAlTqRkeyRX"
access_token_secret = "ZDqtv4zEa9b5u2BYkohIyk29XxjHjp9MFUSVyiBHK8oWh"
consumer_key = "b5FejlayA40AGVfvYZLhRZ9XC"
consumer_secret = "i4EtfR3QD7JF2t8XaBcnqEdViWemsiPt6SDcz2FA0bhnm2baGg"

#Setup the database connection
conn = db.connect(host = '127.0.0.1', user="root", passwd="root", charset="utf8", use_unicode=True)
cur = conn.cursor()

#Select 'twitterdata' as the database to use
cur.execute('USE twitterdata;')

#Setup hashtag regex
hashtagPattern = re.compile('([A-Z])\w+')
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #Make a call to the database to get tweets.
    cur.execute('SELECT T.TweetId FROM Tweets as T;')
    data = cur.fetchall()
    for row in data:
        #Call TweepyAPI to fetch the retweets of each tweet in the DB
        try:
            retweetData =  api.retweets(row[0])
            for status in retweetData:
                stat = json.loads(status)
                retweetId = stat['id']
                retweetCreatedAt = stat['created_at']
                cur.execute('''INSERT INTO Retweets VALUES (%s, %s, %s);''', (userId, retweetId, retweetCreatedAt))
                conn.commit()
        except:
            pass
