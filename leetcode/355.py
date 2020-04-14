class Twitter:
    class User:
        def __init__(self, id):
            self.id = id
            self.posts = []
            self.following = set()
            self.following.add(self.id)

    class Tweet:
        def __init__(self, id):
            self.id = id

    def __init__(self):
        self.tweets = []
        self.users = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = self.User(userId)
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list:
        res = []
        if userId not in self.users:
            return res
        print(userId, 'follows:', self.users[userId].following)
        for tweet in self.tweets[::-1]:
            if tweet[0] in self.users[userId].following:
                res.append(tweet[1])
            if len(res) == 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users:
            self.users[followeeId] = self.User(followeeId)
        if followerId not in self.users:
            self.users[followerId] = self.User(followerId)
        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            return
        if followerId == followeeId:
            return
        if followeeId in self.users[followerId].following:
            self.users[followerId].following.remove(followeeId)


obj = Twitter()


# obj.postTweet(1, 1)
# print(obj.getNewsFeed(1))
# obj.follow(1, 2)
# obj.postTweet(2, 6)
# print(obj.getNewsFeed(1))
# obj.unfollow(1, 2)
# print(obj.getNewsFeed(1))

def run(obj, commands: list, pars: list):
    print(commands[20], pars[20])
    for i in range(1, len(commands)):
        print(i, commands[i], pars[i])
        if commands[i] == 'postTweet':
            obj.postTweet(pars[i][0], pars[i][1])
        if commands[i] == 'getNewsFeed':
            print(obj.getNewsFeed(pars[i][0]))
        if commands[i] == 'follow':
            obj.follow(pars[i][0], pars[i][1])
        if commands[i] == 'unfollow':
            obj.unfollow(pars[i][0], pars[i][1])


run(obj,
    ["Twitter", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
     "postTweet", "postTweet", "getNewsFeed", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
     "postTweet", "postTweet", "postTweet", "getNewsFeed", "postTweet", "unfollow", "postTweet", "postTweet",
     "postTweet", "getNewsFeed", "postTweet", "postTweet", "getNewsFeed", "postTweet", "postTweet", "postTweet",
     "postTweet", "postTweet", "postTweet", "postTweet", "follow", "postTweet", "postTweet", "postTweet", "postTweet",
     "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
     "postTweet", "postTweet", "follow", "postTweet", "postTweet", "postTweet", "postTweet", "follow", "postTweet",
     "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
     "postTweet", "postTweet", "postTweet", "getNewsFeed", "postTweet", "postTweet", "getNewsFeed", "postTweet",
     "postTweet", "follow", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
     "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
     "postTweet", "postTweet", "postTweet", "getNewsFeed", "postTweet", "postTweet", "postTweet", "postTweet",
     "postTweet", "postTweet", "postTweet", "postTweet", "unfollow", "postTweet", "postTweet", "unfollow",
     "getNewsFeed", "postTweet", "postTweet", "follow", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
     "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
     "postTweet", "unfollow", "getNewsFeed", "postTweet", "postTweet", "postTweet", "unfollow", "postTweet",
     "postTweet", "postTweet", "postTweet", "unfollow", "postTweet", "postTweet", "postTweet", "getNewsFeed",
     "postTweet", "postTweet"],
    [[], [11, 994], [4, 303], [1, 113], [18, 309], [8, 905], [6, 605], [1, 210], [15, 15], [1, 88], [1, 704], [8],
     [9, 59], [4, 851], [13, 974], [2, 133], [15, 255], [15, 662], [16, 21], [13, 227], [17], [5, 603], [10, 7],
     [5, 816], [7, 792], [12, 260], [5], [4, 586], [1, 645], [20], [15, 171], [16, 18], [3, 812], [15, 153], [12, 726],
     [6, 508], [17, 817], [5, 6], [3, 667], [5, 599], [13, 353], [11, 282], [7, 226], [18, 423], [13, 875], [2, 738],
     [6, 727], [7, 374], [19, 811], [8, 418], [2, 179], [3, 476], [9, 15], [16, 8], [19, 827], [17, 203], [13, 246],
     [14, 8], [13, 750], [4, 595], [1, 793], [17, 995], [11, 589], [2, 115], [18, 870], [15, 426], [18, 953], [10, 318],
     [10, 419], [2, 164], [9], [18, 854], [3, 394], [17], [4, 834], [4, 349], [2, 16], [13, 534], [3, 773], [4, 292],
     [5, 951], [17, 554], [4, 646], [6, 412], [15, 548], [8, 188], [5, 539], [18, 732], [8, 591], [11, 733], [1, 517],
     [8, 156], [13, 331], [11, 889], [12, 782], [11], [2, 578], [16, 487], [12, 640], [14, 112], [10, 901], [8, 807],
     [7, 818], [7, 627], [14, 9], [4, 522], [7, 505], [9, 13], [3], [1, 971], [18, 808], [1, 17], [7, 197], [7, 361],
     [2, 986], [17, 6], [7, 211], [15, 342], [5, 538], [1, 711], [11, 863], [17, 339], [5, 656], [4, 402], [1, 514],
     [11, 566], [12, 11], [12], [19, 899], [19, 526], [20, 799], [4, 1], [17, 363], [7, 845], [15, 329], [17, 369],
     [18, 18], [15, 848], [5, 928], [18, 105], [18], [17, 785], [11, 457]])
