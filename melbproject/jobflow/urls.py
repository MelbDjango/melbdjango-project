from django.conf.urls import include, url
from .views import (HomePageView, FilterByTagView, VisualView, ShortlistView, countTags, shortListJob)
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^$', HomePageView.as_view(), name='_home'),
    url(r'^viz/$', VisualView.as_view(), name='_viz'),
    url(r'^shortlisted/$', ShortlistView.as_view(), name='_short'),
    url(r'^add/(?P<pk>\d+)/$', shortListJob, name='_add'),
    url(r'^api/count_tags/$', countTags, name='_count_tags'),
    url(r'^(?P<hashtag>\w+)/$', FilterByTagView.as_view(), name='_detail'),
]