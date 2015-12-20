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
		#call stored procedure
		conn = db.connect(host = 'localhost', user="dbproject", passwd="edvictor", db="twitterdata")
		cur = conn.cursor(db.cursors.DictCursor)
		cur.callproc('FindTweetsGivenHashTag', (hashtag,))
		# If the procedure is executed successfully, then we'll commit the changes and return the success message. 
		data = cur.fetchall()
		tuples = list()
		for row in data:
			tuples.append(row)
		return json.dumps({'success': tuples})
	except Exception as e:
		return json.dumps({'error':str(e)})
	finally:
		cur.close()
		conn.close()

if __name__ == "__main__":
    app.run()