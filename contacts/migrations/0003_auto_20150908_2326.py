# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20150908_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phones',
            field=models.ManyToManyField(to='contacts.PhoneNumber'),
        ),
        migrations.AlterField(
            model_name='address',
            name='contact_name',
            field=models.CharField(max_length=1022, blank=True, null=True),
        ),
    ]
