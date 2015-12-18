while true; do
	python twitter_streaming.py
	#$TASK_PID=$!
	#sleep 30
        echo "Streaming done"
	#kill $TASK_PID
	sleep 30
        echo "About to kill DB"
	python nuke_db.py
	python initialize_db.py
done
