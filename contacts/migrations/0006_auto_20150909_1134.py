# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20150909_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonenumber',
            old_name='phone',
            new_name='type',
        ),
    ]
