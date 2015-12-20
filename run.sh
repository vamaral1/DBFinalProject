while true; do
	python twitter_streaming.py
        echo "Streaming done"
	sleep 600
        python retweets.py
        sleep 600 
        echo "About to kill DB and restart"
	python nuke_db.py
	python initialize_db.py
done
