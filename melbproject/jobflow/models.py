from django.db import models
from django.conf import settings


class TwitterUser(models.Model):
    descriptive_name = models.CharField(max_length=200)
    twitter_handle = models.CharField(max_length=200)
    profile_img_url = models.URLField()
    url = models.URLField()
    tagline = models.CharField(max_length=200)

    def __str__(self):
        return'{} @{} - {}'.format(self.descriptive_name, self.twitter_handle, self.tagline)


class Tweet(models.Model):
    text = models.CharField(max_length=200)
    message_id = models.BigIntegerField()
    user = models.ForeignKey('TwitterUser')
    created_at = models.CharField(max_length=200)

    def __str__(self):
        return '{} : {} : {}'.format(self.message_id, self.created_at, self.text)


class HashTag(models.Model):
    name = models.CharField(max_length=200)
    tweet = models.ForeignKey('Tweet')

    def __str__(self):
        return '#{}'.format(self.name)


class ShortListTweet(models.Model):
    tweet = models.ForeignKey('Tweet')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
