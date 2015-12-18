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

#Get starttime
start = datetime.datetime.now()

def get_sentiment(dict_data):
    # pass tweet into TextBlob
    tweet = TextBlob(dict_data["text"])

    # determine if sentiment is positive, negative, or neutral
    if tweet.sentiment.polarity < 0:
        sentiment = "negative"
    elif tweet.sentiment.polarity == 0:
        sentiment = "neutral"
    else:
        sentiment = "positive"
        
    return sentiment

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, stream): 
        data = json.loads(stream)
        #print stream
        
        # USER TABLE
        userId = data['user']['id']                     #user id
        userScreen = data['user']['screen_name']        #user screenname
        userName = data['user']['name']                 #user name
        userFollowers = data['user']['followers_count'] #user followers
        userFollowing = data['user']['friends_count']   #user following
        userStatusCount = data['user']['statuses_count']#user tweets
        userTimeZone = data['user']['time_zone']        #user time zone
        userLanguage = data['user']['lang']             #user language

        if(not cur.fetchone()):
            cur.execute('''INSERT INTO Users VALUES (%s, %s, %s, %s, %s, %s, %s);''', (userId, userScreen, userName, userFollowers, userFollowing, userStatusCount, userLanguage))
            conn.commit()

        # TWEETS TABLE
        tweetId = data['id']                      #tweet id
        tweetCreatedAt = data['created_at']       #tweet creation time
        tweetText = data['text']
        #print data['coordinates']   #TODO - coordinates
        tweetLatitude = "temp"
        tweetLongitude = "tmp"
        tweetSentiment = get_sentiment(data)
        cur.execute('''INSERT INTO Tweets VALUES (%s, %s, %s, %s, %s, %s, %s);''',(tweetId, userId, tweetCreatedAt, tweetText, tweetSentiment, tweetLatitude, tweetLongitude))
        conn.commit()

        # FOLLOWERS TABLE
        #for follower in tweepy.Cursor(api.followers, screen_name=userScreen).items():
        #    followerId = follower.id
        #    print followerId
        #    cur.execute('''INSERT INTO Followers VALUES (%s, %s);''', (userId, followerId))
        #    conn.commit()
        #    time.sleep(10)

        # FAVORITES TABLE
        #for favorited in tweepy.Cursor(api.favorites, screen_name=userScreen).items():
        #    favoriteId = favorited.id
        #    favoritedAt = favorited.created_at
        #    cur.execute('''INSERT INTO Favorites VALUES (%s, %s, %s);''', (favoriteId, userId, favoritedAt))
        #    conn.commit()
    
        # RETWEETS TABLE
        #print "\n\n\nABOUT TO SLEEP\n\n\n"
        #time.sleep(120)
        #retweets = api.retweets(tweetId)
        #print retweets
        #time.sleep(10)

        # HASHTAGS TABLE
        hashTagList = data['entities']['hashtags']
        for hashTagEntity in hashTagList:
            m = hashtagPattern.search(str(hashTagEntity))
            if m is not None:
                cur.execute('''INSERT INTO Hashtags VALUES (%s, %s);''', (tweetId, m.group()))
                conn.commit()

        # MEDIA TABLE
        try:
            mediaId = data['entities']['media'][0]["id_str"]
            mediaUrl = data['entities']['media'][0]["url"]
            mediaType = data['entities']['media'][0]["type"]
            mediaH = data['entities']['media'][0]["sizes"]["small"]["h"]
            mediaW = data['entities']['media'][0]["sizes"]["small"]["w"]
            cur.execute('''INSERT INTO Media VALUES (%s, %s, %s, %s, %s, %s);''', (mediaId, tweetId, mediaUrl, mediaType, mediaH, mediaW))
            conn.commit()
        except:
            pass


        end = datetime.datetime.now()
        elapsed = end-start
        if elapsed > datetime.timedelta(minutes=1):
            sys.exit("Script time up")

        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    stream = Stream(auth, l)

    stream.filter(track=['retweet'])
