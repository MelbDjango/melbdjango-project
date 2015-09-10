from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
)
