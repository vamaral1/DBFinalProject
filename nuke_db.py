import MySQLdb as db

conn = db.connect(host = '127.0.0.1', user="root", passwd="root")
cur = conn.cursor()

#delete database
cur.execute('DROP DATABASE twitterdata;')

conn.commit()
conn.close()