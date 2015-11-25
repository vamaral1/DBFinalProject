import MySQLdb as db

conn = db.connect(host = '127.0.0.1', user="root", passwd="root")
cur = conn.cursor()

#create database if it doesn't exist
cur.execute('CREATE DATABASE IF NOT EXISTS twitterdata;')

#select twitterdata as the database to use
cur.execute('USE twitterdata;')

#create tables
cur.execute('''CREATE TABLE IF NOT EXISTS Users(
                UserId INT,
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
                TweetId INT,
                UserId INT,
                Time BIGINT,
                Content VARCHAR(100),
                Lat VARCHAR(25),
                Lon VARCHAR(25),
                PRIMARY KEY (TweetId, UserId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Favorites(
                TweetId INT,
                UserId INT,
                Time BIGINT,
                PRIMARY KEY (TweetId, UserId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Followers(
                WhoIsFollowedId INT,
                WhoFollowsId INT,
                PRIMARY KEY (WhoIsFollowedId, WhoFollowsId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Retweets(
                TweetId INT,
                RetweeterId INT,
                Time BIGINT,
                PRIMARY KEY (TweetId, RetweeterId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Hashtags(
                TweetId INT,
                Hashtag VARCHAR(50),
                PRIMARY KEY (TweetId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Media(
				MediaId INT,
                TweetId INT,
                Link VARCHAR(100),
                Type VARCHAR(25),
                Height INT,
                Width INT,
                PRIMARY KEY (MediaId,TweetId)
                );
            ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Mentions(
                TweetId INT,
                WhoIsMentionedId INT,
                WhoMentions INT,
                PRIMARY KEY (TweetId)
                );
            ''')
conn.close()