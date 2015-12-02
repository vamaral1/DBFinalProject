import MySQLdb as db
import re

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
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

#utf8mb4 = re.compile(u'[U00010000-U0010ffff]')

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, stream): 
        #data = utf8mb4.sub(u'', stream.json)
        data = json.loads(stream)
        
        # USER TABLE
        userId = data['user']['id']                      #user id
        print userId
        userScreen = data['user']['screen_name']        #user screenname
        userName = data['user']['name']                  #user name
        userFollowers = data['user']['followers_count']  #user followers
        userFollowing = data['user']['friends_count']    #user following
        userStatusCount = data['user']['statuses_count'] #user tweets
        userTimeZone = data['user']['time_zone']         #user time zone
        userLanguage = data['user']['lang']              #user language

        # Insert data from the tweet into the User table
        cur.execute('''INSERT INTO Users VALUES (%s, %s, %s, %s, %s, %s, %s);''', (userId, userScreen, userName, userFollowers, userFollowing, userStatusCount, userLanguage))
        conn.commit()

        # TWEETS TABLE
        print data['id']                      #tweet id
        print data['user']['id']              #user id
        print data['created_at']              #tweet creation time
        print data['text']
        print data['coordinates']

        print "\n"

        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['kobe'])
