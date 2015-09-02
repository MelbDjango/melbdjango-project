from django.conf.urls import include, url
from .views import (HomePageView, FilterByTagView)

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='_home'),
    url(r'^(?P<hashtag>\w+)/$', FilterByTagView.as_view(), name='_detail'),
]