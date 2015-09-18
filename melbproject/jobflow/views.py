from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.http import JsonResponse, HttpResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Tweet, HashTag, ShortListTweet
from .tweets import Twitterbot

class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class HomePageView(TemplateView):

    template_name = 'default.html'

    def __init__(self, **kwargs):
        super(HomePageView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['tags'] = HashTag.objects.all().values('name').distinct()
        
        tweets = Tweet.objects.all()
        if self.request.user.is_authenticated():
            shortlist = ShortListTweet.objects.filter(author=self.request.user)
            shortlist = [ item.tweet for item in shortlist ]
            blah = []
            for tweet in tweets:
                tweet.ticked = False
                if tweet in shortlist:
                    tweet.ticked = True
                blah.append(tweet)
            tweets = blah
        context['tweets'] = tweets
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


class ShortlistView(LoginRequiredMixin, ListView):

    model = ShortListTweet
    template_name = 'shortlist.html'

    def get_queryset(self):
        queryset = super(ShortlistView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ShortlistView, self).get_context_data(**kwargs)
        shortlist = self.get_queryset()
        context['tweets'] = [item.tweet for item in shortlist]
        return context


@login_required
def shortListJob(request, pk):
    shortlist = ShortListTweet()
    shortlist.author = request.user
    shortlist.tweet = get_object_or_404(Tweet, pk=pk)
    shortlist.save()
    return redirect('_home')


def countTags(request):
    tagsummary = HashTag.objects.values("name").annotate(size=Count('id')).order_by()
    tagdata = {}
    for t in tagsummary:
        hashtag = t['name']
        size = t['size']
        tagdata[hashtag] = size
    return JsonResponse(tagdata, safe=False)
