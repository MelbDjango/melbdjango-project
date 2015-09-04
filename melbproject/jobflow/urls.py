from django.conf.urls import include, url
from .views import (HomePageView, FilterByTagView, VisualView, countTags)

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='_home'),
    url(r'^viz/$', VisualView.as_view(), name='_viz'),
    url(r'^api/count_tags/$', countTags, name='_count_tags'),
    url(r'^(?P<hashtag>\w+)/$', FilterByTagView.as_view(), name='_detail'),
]