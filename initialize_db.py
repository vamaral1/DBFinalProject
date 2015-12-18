import MySQLdb as db

conn = db.connect(host = 'localhost', user="dbproject", passwd="edvictor")
cur = conn.cursor()

#create database if it doesn't exist
cur.execute('CREATE DATABASE IF NOT EXISTS twitterdata;')

#select twitterdata as the database to use
cur.execute('USE twitterdata;')

#create tables
cur.execute('''CREATE TABLE IF NOT EXISTS Users(
                UserId BIGINT,
                ScreenName VARCHAR(25),
                Name VARCHAR(25),
                NumFollowers INT,
                NumFollowing INT,
                NumPosts INT,
                Language VARCHAR(25)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Tweets(
                TweetId BIGINT,
                UserId BIGINT,
                Time BIGINT,
                Content VARCHAR(5000),
                Sentiment VARCHAR(25),
                Lat VARCHAR(25),
                Lon VARCHAR(25)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Favorites(
                TweetId BIGINT,
                UserId BIGINT,
                Time BIGINT
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Followers(
                WhoIsFollowed BIGINT,
                WhoFollows BIGINT
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Retweets(
                TweetId BIGINT,
                RetweeterId BIGINT,
                Time BIGINT
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Hashtags(
                TweetId BIGINT,
                Hashtag VARCHAR(50)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Media(
				MediaId BIGINT,
                TweetId BIGINT,
                Link VARCHAR(100),
                Type VARCHAR(25),
                Height INT,
                Width INT
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Mentions(
                TweetId BIGINT,
                WhoIsMentioned BIGINT,
                WhoMentions BIGINT
                );
            ''')
conn.close()
