/* Rank users by their followers:following ratio */
SELECT UserId, ScreenName, NumFollowers/NumFollowing AS FollowersToFollowingRatio FROM Users ORDER BY FollowersToFollowingRatio;

/* Select the 5 users with the most positive sentiment tweets */
SELECT U.ScreenName, count(TweetId) as PositiveTweetCount FROM Users AS U, Tweets as T WHERE U.UserId = T.UserId and T.Sentiment = "positive" group by U.ScreenName ORDER BY PositiveTweetCount LIMIT 5;

/* Select all positive setiment tweets with the "Warriors" hashtag  */
SELECT T.Content From Tweets AS T, Hashtags AS H WHERE T.TweetId = H.TweetId and T.Sentiment = "positive";
