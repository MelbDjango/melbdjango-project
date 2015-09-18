from django.contrib import admin
from .models import (HashTag, Tweet, TwitterUser, ShortListTweet)

admin.site.register(HashTag)
admin.site.register(Tweet)
admin.site.register(TwitterUser)
#admin.site.register(ShortListTweet)

