# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20150908_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='contact_name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='emails',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phones',
        ),
        migrations.AddField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(to='contacts.Contact', null=True),
        ),
        migrations.AddField(
            model_name='email',
            name='contact',
            field=models.ForeignKey(to='contacts.Contact', null=True),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='contact',
            field=models.ForeignKey(to='contacts.Contact', null=True),
        ),
    ]
