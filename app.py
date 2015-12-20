from flask import Flask, render_template, request, json
import MySQLdb as db
import pdb

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/tweetsHashtag",methods=['POST','GET'])
def tweetsHashtag():
	try:
		hashtag = request.form['inputName']
		print hashtag
		#call stored procedure
		conn = db.connect(host = 'localhost', user="dbproject", passwd="edvictor", db="twitterdata")
		cur = conn.cursor()
		cur.callproc('FindTweetsGivenHashTag', (hashtag,))
		# If the procedure is executed successfully, then we'll commit the changes and return the success message. 
		# data = cur.fetchall()
		# print type(data)
		# for row in data:
		# 	print row
		data = mysql.fetchall()
		print '<table border="0"><tr><th>TweetId</th><th>UserId</th><th>Time</th><th>Content</th><th>Sentiment</th><th>Lat</th><th>Lon</th></tr>'
		print '<tbody>'
		pdb.set_trace()
		for row in data:
			print '<tr><td>' + row[0] + '</td><td>' + row[1] + '</td><td>' + row[2] + '</td><td>' + row[3] + '</td><td>' + row[4] + '</td><td>' + row[5] + '</td><td>' + row[6] +  '</td><td></td></tr>'
		print '</tbody>'
		print '</table>'
	except Exception as e:
		return json.dumps({'error':str(e)})
	finally:
		cur.close()
		conn.close()

if __name__ == "__main__":
    app.run()