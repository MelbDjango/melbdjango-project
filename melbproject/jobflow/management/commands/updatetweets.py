from django.core.management.base import BaseCommand, CommandError
from jobflow import tweets

class Command(BaseCommand):
    help = 'refresh timeline of a twitter account'

    def add_arguments(self, parser):
        parser.add_argument('num_tweets', nargs='+', type=int)

    def handle(self, *args, **options):
        for num_tweets in options['num_tweets']:
            timeline = tweets.Twitterbot(num_tweets)
            timeline.refresh()

            self.stdout.write('Successfully refreshed twitter feed')

