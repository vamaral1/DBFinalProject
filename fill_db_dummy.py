import MySQLdb as db

conn = db.connect(host = '127.0.0.1', user="root", passwd="root")
cur = conn.cursor()

#select twitterdata as the database to use
cur.execute('USE twitterdata;')

#insert dummy data
cur.execute('''INSERT INTO Users VALUES
	(12345, '@_victorama', 'Victor Amaral', 82, 131, 23, 'English')
	''')

cur.execute('''INSERT INTO Users VALUES
	(6789, '@schembor', 'Ed Schembor', 45, 141, 45, 'English')
	''')

cur.execute('''INSERT INTO Tweets VALUES
	(8950345, 12345, 53256734, "Testing tweet tweet", "-74.0005941", "40.7122784")
	''')

cur.execute('''INSERT INTO Favorites VALUES
	(8950345, 12345, 7645262)
	''')

cur.execute('''INSERT INTO Followers VALUES
	(12345, 6789)
	''')

cur.execute('''INSERT INTO Retweets VALUES
	(8950345, 6789, 91238323)
	''')

cur.execute('''INSERT INTO Hashtags VALUES
	(8950345, "#webscale")
	''')

cur.execute('''INSERT INTO Media VALUES
	(84656, 8950345, "https://www.youtube.com/watch?v=b2F-DItXtZs", "Video", 720, 1080)
	''')

cur.execute('''INSERT INTO Mentions VALUES
	(8950345, 6789, 12345)
	''')

conn.commit()
conn.close()