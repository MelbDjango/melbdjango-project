import TwitterAPI


class Twitterbot(object):

    consumer_key = 'Ktp2lfQ69lw6ZIfJjr1w3JBq5'
    consumer_secret = 'bTV73VkoH6bRH3JmcWIBh2TEH5Dhdzltl9bqcFFF715jXNPlJ4'
    api = None
    response = None
    tweets = []
    hashtags = {}

    def __init__(self, tweet_count=200, twitter_account='stackdevjobs'):
        self.api = TwitterAPI.TwitterAPI(
            self.consumer_key,
            self.consumer_secret,
            auth_type='oAuth2'
        )
        self.response = self.api.request(
            'statuses/user_timeline',
            {'screen_name': twitter_account,
             'count': tweet_count})

        self.readTweets()

    def readTweets(self):
        count = 0
        for tweet in self.response.get_iterator():
            if tweet['text'] and tweet['entities']['hashtags']:
                item = {}
                count += 1
                item['id'] = count
                item['text'] = tweet['text']
                tags = []
                for tag in tweet['entities']['hashtags']:
                    key = tag['text']
                    tags.append(key)
                    if key not in self.hashtags:
                        self.hashtags[key] = [count]
                    else:
                        self.hashtags[key].append(count)
                item['hashtags'] = tags
                self.tweets.append(item)
        # print(self.hashtags)
        # print(self.tweets)

    def getHashTags(self):
        return self.hashtags.keys()

    def getTweets(self, hashtag=None):
        if not hashtag:
            return self.tweets
        else:
            return self.filterTweets(hashtag)

    def filterTweets(self, hashtag):
        return [tweet for tweet in self.tweets if hashtag in tweet['hashtags']]

# x = Twitterbot(3)
# print(x.filterTweets("java"))
# print(x.getTweets())

