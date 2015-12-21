/* Rank users by their followers:following ratio */
SELECT UserId, ScreenName, NumFollowers/NumFollowing AS FollowersToFollowingRatio FROM Users ORDER BY FollowersToFollowingRatio;

/* Select the 5 users with the most positive sentiment tweets */
SELECT U.ScreenName, count(TweetId) as PositiveTweetCount FROM Users AS U, Tweets as T WHERE U.UserId = T.UserId and T.Sentiment = "positive" group by U.ScreenName ORDER BY PositiveTweetCount LIMIT 5;

/* Select all positive setiment tweets with the "Warriors" hashtag  */
SELECT T.Content From Tweets AS T, Hashtags AS H WHERE T.TweetId = H.TweetId and T.Sentiment = "positive";

/* Give the link to the largest picture */
SELECT M.Link as LargestPictureLink FROM Media as M, (SELECT max(Height*Width) as maxArea FROM Media) as Max WHERE M.Height*M.Width = Max.maxArea;

/* Give all users who have tweeted a picture with the “NBA” hashtag */
SELECT U.Name FROM Media as M, Tweets as T, Users as U, Hashtags as H WHERE M.TweetId = T.TweetId AND H.TweetId = T.TweetId AND H.Hashtag = "NBA" AND U.UserId = T.UserId;

/* Find the percentage of tweets with the “Clinton” hashtag that have positive sentiment */
SELECT Tot.total, pos.positive, (pos.positive/Tot.total) as PercentPositive FROM (SELECT count(T.TweetId) as Total FROM Tweets as T, Hashtags as H WHERE T.TweetId = H.TweetId AND H.Hashtag = 'Clinton') as Tot, (SELECT count(T.TweetId) as Positive FROM Tweets as T, Hashtags as H WHERE T.TweetId = H.TweetId AND H.Hashtag = 'Clinton' AND T.Sentiment = "Positive") as pos;

/* Find all tweets posted by someone who has the “NBA” text pattern in their username */
SELECT T.Content FROM Users as U, Tweets as T WHERE U.ScreenName Like '%NBA%' AND U.UserId = T.UserId;

/*Find the users who have their username, any tweets, or any hashtags with the “mongo db” or “webscale” text patterns in them */
SELECT U.ScreenName FROM Tweets as T, Users as U, Hashtags as H WHERE T.UserId = U.UserId AND T.TweetId = H.TweetId AND T.Content Like "%mongo db%" OR T.Content Like "%webscale%" OR U.ScreenName LIKE "%mongo db%" OR U.ScreenName LIKE "%webscale%" OR H.Hashtag LIKE "%mongo db%" OR H.Hashtag LIKE "%webscale%";

/*Show the percentage of each sentiment for tweets, gender of the user posted, and the language posted in from users who are using one of the top 10 languages used currently*/
SELECT Tweets.Sentiment, (COUNT(Tweets.TweetId) * 100/(SELECT COUNT(*) FROM Tweets)) as Percentage
FROM Tweets
GROUP BY Tweets.Sentiment;
SELECT Users.Language, Count(*) AS NumTimesUsed
FROM Users
GROUP BY Users.Language
ORDER BY NumTimesUsed DESC LIMIT 10;

/* Find the users who have liked the most posts and return the hashtags that this user’s used */
SELECT H.Hashtag FROM (SELECT UserId, count(TweetId) as FavCount, M.maxFav FROM Favorites, (SELECT max(F.FavCount) as maxFav FROM (SELECT count(TweetId) as FavCount From Favorites group by UserId) as F) as M group by UserId) as countAndMax, Tweets as T, Hashtags as H WHERE countAndMax.FavCount = countAndMax.maxFav and T.UserId = countAndMax.UserId and T.TweetId = H.TweetId;


/* Find all users who have created a tweet with a palindrome ID & their total number of tweets */
SELECT T.TweetId, U.ScreenName, U.NumPosts From Tweets as T, Users as U WHERE T.UserId = U.UserId and T.TweetId = Reverse(T.TweetId);

/* Find the sentiment of all tweets from a specified user and then show all tweets with positive sentiment which have a specified hashtag. */
DELIMITER //
DROP PROCEDURE IF EXISTS FindUserSentimentAndHash;
CREATE PROCEDURE FindUserSentimentAndHash(IN screenname VARCHAR(25), IN hashtag VARCHAR(25))
BEGIN
IF EXISTS(SELECT T.Sentiment FROM Tweets as T, Users as U WHERE T.UserId = U.UserId and U.ScreenName = screenname) THEN
    BEGIN
	CALL FindUserSentiment(screenname);
           SELECT T.Content FROM Users as U, Hashtags as H, Tweets as T WHERE H.TweetId = T.TweetId and U.UserId = T.UserId and T.Sentiment = "positive" and H.Hashtag = hashtag;
	END;
ELSE
    BEGIN
	SELECT "User not found";
	END;
END IF;
END//
DELIMITER ;

/* Find all users who have over a specified amount of tweets and return their longest tweet*/
DELIMITER //
DROP PROCEDURE IF EXISTS TweetCountAndLongest;
CREATE PROCEDURE TweetCountAndLongest(IN tweetCount INT)
BEGIN
IF EXISTS(SELECT U.UserId, T.Content FROM Users as U, Tweets as T, (SELECT max(length(T.Content)) as MaxLen, T.UserId FROM Tweets as T group by UserId) as MLS WHERE MLS.UserId = U.UserId and T.UserId = U.UserId and length(T.Content) = MLS.MaxLen and U.NumPosts > tweetCount) THEN
    BEGIN
	SELECT U.UserId, T.Content FROM Users as U, Tweets as T, (SELECT max(length(T.Content)) as MaxLen, T.UserId FROM Tweets as T group by UserId) as MLS WHERE MLS.UserId = U.UserId and T.UserId = U.UserId and length(T.Content) = MLS.MaxLen and U.NumPosts > tweetCount;
	END;
ELSE
    BEGIN
	SELECT "User not found";
	END;
END IF;
END//
DELIMITER ;

/*Display the top 10 tweets that contain a user-specified word*/
DELIMITER //
DROP PROCEDURE IF EXISTS FindTweetsGivenWord(IN word VARCHAR(25));
CREATE PROCEDURE FindTweetsGivenWord(IN word VARCHAR(25))
BEGIN
IF EXISTS(SELECT * FROM Tweets WHERE Tweets.Content LIKE word) THEN
    BEGIN
	SELECT * FROM Tweets WHERE Tweets.Content LIKE word;
	END;
ELSE
    BEGIN
	SELECT "Word not found";
	END;
END IF;
END//
DELIMITER ;

/*Find the tweets with user-specified hashtag*/
DELIMITER //
DROP PROCEDURE IF EXISTS FindTweetsGivenHashTag;
CREATE PROCEDURE FindTweetsGivenHashTag(IN hashtag VARCHAR(25))
BEGIN
IF EXISTS(SELECT * FROM Hashtags WHERE Hashtags.Hashtag = hashtag) THEN
    BEGIN
	SELECT * FROM Tweets WHERE Tweets.TweetId IN (Select Hashtags.TweetId FROM Hashtags WHERE Hashtags.Hashtag = hashtag);
	END;
ELSE
    BEGIN
	SELECT "Hashtag not found";
	END;
END IF;
END//
DELIMITER ;
