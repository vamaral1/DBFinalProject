#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2714753071-RMkfVbxgUKowUwW0xUYAk8cVpQDFKAlTqRkeyRX"
access_token_secret = "ZDqtv4zEa9b5u2BYkohIyk29XxjHjp9MFUSVyiBHK8oWh"
consumer_key = "b5FejlayA40AGVfvYZLhRZ9XC"
consumer_secret = "i4EtfR3QD7JF2t8XaBcnqEdViWemsiPt6SDcz2FA0bhnm2baGg"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
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
    stream.filter(track=['python', 'javascript', 'ruby'])