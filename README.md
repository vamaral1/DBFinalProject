# DBFinalProject

Streaming twitter data to database with front-end to query certain topics

## Authors:
Victor Amaral

Edward Schembor

## Setting up the database
We initialized an AWS EC2 instance (which is now terminated) and installed MySQL

A MySQL account has already been created on the instance but if needed, this is how to do it:

  * mysql -u root -p (note: the root password is root)
  * mysql > CREATE USER 'dbproject'@'localhost' IDENTIFIED BY 'edvictor';
  * mysql > GRANT ALL PRIVILEGES ON \*.\* TO 'dbproject'@'localhost' WITH GRANT OPTION;
  * mysql > quit;

Next, run <code>python initialize_db.py</code>

Now login to the database and you'll see that the database "twitterdata" has been created with all its tables

  * mysql -u dbproject -p (note: the password is edvictor)
  * mysql > USE twitterdata;
  * mysql > SHOW TABLES;

To fill in the database with some dummy values you can also run <code>python fill_db_dummy.py</code> and reset the database using <code>python nuke_db.py</code>
