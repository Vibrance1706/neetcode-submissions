class Twitter:

    def __init__(self):
        self.dict_post_tweet = {}
        self.follow_list = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.dict_post_tweet:
            self.dict_post_tweet[userId] = [(self.time, userId, tweetId)]
        else:
            self.dict_post_tweet[userId].append((self.time, userId, tweetId))

        self.time+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweet_list = []
        if userId in self.dict_post_tweet:
            tweet_list += self.dict_post_tweet[userId]

        if userId in self.follow_list:
            for followeeId in self.follow_list[userId]:
                if followeeId in self.dict_post_tweet:
                    tweet_list += self.dict_post_tweet[followeeId]

        tweet_list.sort(reverse=True)
        tweet_id_list = [tweet_id for _, _, tweet_id in tweet_list[:10]]
        return tweet_id_list
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        if followerId not in self.follow_list:
            self.follow_list[followerId] = []
        
        if followeeId not in self.follow_list[followerId]:
            self.follow_list[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_list:
            if followeeId in self.follow_list[followerId]:
                self.follow_list[followerId].remove(followeeId)
