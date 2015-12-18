from flask import Flask, render_template, request, json
import MySQLdb as db
#from flask.ext.mysql import MySQL

app = Flask(__name__)
#mysql = MySQL()
# MySQL configurations
# app.config['MYSQL_DATABASE_USER'] = 'dbproject'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'edvictor'
# app.config['MYSQL_DATABASE_DB'] = 'twitterdata'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)
# conn = mysql.connect()
# cur = conn.cursor()
conn = db.connect(host = 'localhost', user="dbproject", passwd="edvictor", db="twitterdata")
cur = conn.cursor()

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/tweetsHashtag",methods=['POST','GET'])
def tweetsHashtag():
	#try:
	hashtag = request.form['inputName']
	print type(hashtag)
	#call stored procedure
	cur.callproc('FindTweetsGivenHashTag', (hashtag))
	print "I came 3 times"
	# If the procedure is executed successfully, then we'll commit the changes and return the success message. 
	data = cur.fetchall()
	if len(data) is 0:
	    conn.commit()
	    return json.dumps({'message':'Query successful!'})
	else:
	    return json.dumps({'error':str(data[0])})
	# except Exception as e:
	# 	return json.dumps({'error':str(e)})
	# finally:
	# 	cur.close()
	# 	conn.close()

if __name__ == "__main__":
    app.run()