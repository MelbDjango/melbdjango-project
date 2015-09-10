# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.TextField(blank=True)),
                ('start', models.DateTimeField(blank=True)),
                ('end', models.DateTimeField(blank=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('contacts', models.ManyToManyField(to='contacts.Contact')),
            ],
            options={
                'ordering': ('-start', 'description'),
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('abbrev', models.CharField(max_length=6)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True)),
                ('table', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.TextField()),
                ('address', models.ForeignKey(to='contacts.Address')),
                ('contacts', models.ManyToManyField(to='contacts.Contact')),
            ],
            options={
                'ordering': ('name', 'address'),
            },
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(to='events.EventType'),
        ),
        migrations.AddField(
            model_name='event',
            name='venues',
            field=models.ManyToManyField(to='events.Venue'),
        ),
    ]
