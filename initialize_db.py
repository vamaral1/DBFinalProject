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
                Language VARCHAR(25),
                PRIMARY KEY (UserId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Tweets(
                TweetId BIGINT,
                UserId BIGINT,
                Time BIGINT,
                Content VARCHAR(5000),
                Lat VARCHAR(25),
                Lon VARCHAR(25),
                PRIMARY KEY (TweetId, UserId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Favorites(
                TweetId BIGINT,
                UserId BIGINT,
                Time BIGINT,
                PRIMARY KEY (TweetId, UserId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Followers(
                WhoIsFollowedId BIGINT,
                WhoFollowsId BIGINT,
                PRIMARY KEY (WhoIsFollowedId, WhoFollowsId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Retweets(
                TweetId BIGINT,
                RetweeterId BIGINT,
                Time BIGINT,
                PRIMARY KEY (TweetId, RetweeterId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Hashtags(
                TweetId BIGINT,
                Hashtag VARCHAR(50),
                PRIMARY KEY (TweetId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Media(
				MediaId BIGINT,
                TweetId BIGINT,
                Link VARCHAR(100),
                Type VARCHAR(25),
                Height INT,
                Width INT,
                PRIMARY KEY (MediaId,TweetId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Mentions(
                TweetId BIGINT,
                WhoIsMentionedId BIGINT,
                WhoMentions BIGINT,
                PRIMARY KEY (TweetId)
                );
            ''')
conn.close()
