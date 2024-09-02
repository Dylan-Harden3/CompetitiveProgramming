class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = defaultdict(set)
        self.t = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heappush(self.tweets, [-self.t, userId, tweetId])
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        cur = []
        feed = []
        while self.tweets and len(feed) < 10:
            time, user, tweetId = heappop(self.tweets)
            if user == userId or user in self.follows[userId]:
                feed.append(tweetId)
            cur.append([time, user, tweetId])
        while cur:
            heappush(self.tweets, cur.pop())
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
