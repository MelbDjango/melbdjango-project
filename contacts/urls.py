from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.ContactListView.as_view(), name='contacts'),
    url(r'^new/$', views.ContactCreateView.as_view(), name='contacts_new'),
    url(r'^(?P<pk>\d+)$', views.ContactUpdateView.as_view(), name='contacts_edit'),
    url(r'^(?P<pk>\d+)/del$', views.ContactDeleteView.as_view(), name='contacts_delete'),
    url(r'^(?P<pk>\d+)/addr$', views.ContactAddressView.as_view(), name='contacts_address'),
    url(r'^(?P<pk>\d+)/phone$', views.ContactPhoneView.as_view(), name='contacts_phonenumber'),
    url(r'^(?P<pk>\d+)/email$', views.ContactEmailView.as_view(), name='contacts_email'),
)

