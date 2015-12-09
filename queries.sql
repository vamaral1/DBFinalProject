/*Rank users by their followers:following ratio*/
select UserId, ScreenName, NumFollowers/NumFollowing as FollowersToFollowingRatio from Users order by FollowersToFollowingRatio;
