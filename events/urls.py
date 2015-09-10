from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
   url(r'^$', views.EventListView.as_view(), name='events'),
)
