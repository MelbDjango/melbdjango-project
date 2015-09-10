import os
from django.db.models import Max
import TwitterAPI
from .models import (TwitterUser, Tweet, HashTag)


class Twitterbot(object):

    consumer_key = 'Ktp2lfQ69lw6ZIfJjr1w3JBq5'
    consumer_secret = os.environ.get('TWITTERAPI_CONSUMER_SECRET', None)
    api = None
    response = None
    max_id = None
    first_time = True
    twitter_account = None
    tweet_count = None

    def __init__(self, tweet_count=200, twitter_account='stackdevjobs'):

        self.tweet_count = tweet_count
        self.twitter_account = twitter_account

        self.api = TwitterAPI.TwitterAPI(
            self.consumer_key,
            self.consumer_secret,
            auth_type='oAuth2'
        )

        # get the timeline without max_id
        self.response = self.api.request(
            'statuses/user_timeline',
            {'screen_name': self.twitter_account,
             'count': self.tweet_count})

        self.readTweets()

    def readTweets(self):
        count = 0
        for tweet in self.response.get_iterator():
            if tweet['text'] and tweet['entities']['hashtags']:
                if self.first_time:
                    """Parse for the user info during the first call"""
                    tu = TwitterUser()
                    tu.descriptive_name = tweet['user']['name']
                    tu.twitter_handle = tweet['user']['screen_name']
                    tu.profile_img_url = tweet['user']['profile_image_url']
                    tu.url = tweet['user']['url']
                    tu.save()
                    self.first_time = False

                # save the tweet
                tw = Tweet()
                tw.text = tweet['text']
                tw.created_at = tweet['created_at']
                tw.message_id = tweet['id']
                tw.user = TwitterUser.objects.last()
                tw.save()

                # look for hashtags
                for tag in tweet['entities']['hashtags']:
                    hashtag, created = HashTag.objects.get_or_create(name=tag['text'])
                    
                    if created:
                        hashtag.save()
                        hashtag.tweet.add(tw)

                count += 1
        print("found ", count, "new tweets")

    def refresh(self):
        # get the last tweet that has the largest id so far
        max = Tweet.objects.all().aggregate(Max('message_id'))
        self.max_id = max['message_id__max'] - 1
        print(self.max_id)

        # make the request
        self.response = self.api.request(
            'statuses/user_timeline',
            {'screen_name': self.twitter_account,
             'count': self.tweet_count,
             'max_id': self.max_id})

        self.readTweets()


"""    def getHashTags(self):
        return self.hashtags.keys()

    def getHashTagData(self):
        return self.hashtags

    def getTweets(self, hashtag=None):
        if not hashtag:
            return self.tweets
        else:
            return self.filterTweets(hashtag)

    def filterTweets(self, hashtag):
        return [tweet for tweet in self.tweets if hashtag in tweet['hashtags']]
"""
