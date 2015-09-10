from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.db.models import Count
from .models import Tweet, HashTag
from .tweets import Twitterbot


class HomePageView(TemplateView):

    template_name = 'default.html'

    def __init__(self, **kwargs):
        super(HomePageView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['tags'] = HashTag.objects.all().values('name').distinct()
        context['tweets'] = Tweet.objects.all()
        return context


class FilterByTagView(TemplateView):

    template_name = 'default.html'

    def __init__(self, **kwargs):
        super(FilterByTagView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(FilterByTagView, self).get_context_data(**kwargs)
        hashtag = kwargs.get('hashtag')
        context['tags'] = HashTag.objects.all().values('name').distinct()
        context['tweets'] = Tweet.objects.filter(hashtag__name=hashtag)
        return context


class VisualView(TemplateView):

    template_name = 'viz.html'

    def __init__(self, **kwargs):
        super(VisualView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(VisualView, self).get_context_data(**kwargs)
        context['tweets'] = Tweet.objects.all()
        return context


def countTags(request):
    tagsummary = HashTag.objects.values("name").annotate(size=Count('id')).order_by()
    tagdata = {}
    for t in tagsummary:
        hashtag = t['name']
        size = t['size']
        tagdata[hashtag] = size
    return JsonResponse(tagdata, safe=False)
