# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShortListTweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
                ('message_id', models.BigIntegerField()),
                ('created_at', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('descriptive_name', models.CharField(max_length=200)),
                ('twitter_handle', models.CharField(max_length=200)),
                ('profile_img_url', models.URLField()),
                ('url', models.URLField()),
                ('tagline', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(to='jobflow.TwitterUser'),
        ),
        migrations.AddField(
            model_name='shortlisttweet',
            name='tweet',
            field=models.ForeignKey(to='jobflow.Tweet'),
        ),
        migrations.AddField(
            model_name='hashtag',
            name='tweet',
            field=models.ManyToManyField(to='jobflow.Tweet'),
        ),
    ]
