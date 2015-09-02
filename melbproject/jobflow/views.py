from django.shortcuts import render
from django.views.generic import TemplateView
from .tweets import Twitterbot

data = Twitterbot(10)


class HomePageView(TemplateView):

    template_name = 'default.html'

    def __init__(self, **kwargs):
        super(HomePageView, self).__init__(**kwargs)
        # self.data = Twitterbot(10)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['tags'] = data.getHashTags()
        context['tweets'] = data.getTweets()
        return context


class FilterByTagView(TemplateView):

    template_name = 'default.html'

    def __init__(self, **kwargs):
        super(FilterByTagView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(FilterByTagView, self).get_context_data(**kwargs)
        hashtag = kwargs.get('hashtag')
        context['tags'] = data.getHashTags()
        context['tweets'] = data.getTweets(hashtag)
        return context
