# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20150909_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.CharField(max_length=16, choices=[(None, 'Unspecified'), ('Home', 'Home'), ('Work', 'Work'), ('Main', 'Main'), ('Branch', 'Branch'), ('Mailing', 'Mail'), ('Billing', 'Billing'), ('Legal', 'Legal'), ('Campus', 'Campus'), ('Dormitory', 'Dormitory'), ('Other', 'Other')], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='type',
            field=models.CharField(max_length=16, choices=[(None, 'Unspecified'), ('Home', 'Home'), ('Work', 'Work'), ('Campus', 'Campus'), ('Dormitory', 'Dormitory'), ('Other', 'Other')], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='type',
            field=models.CharField(max_length=16, choices=[(None, 'Unspecified'), ('Home', 'Home'), ('Work', 'Work'), ('Main', 'Main'), ('A/H', 'After Hours'), ('Campus', 'Campus'), ('Dormitory', 'Dormitory'), ('Other', 'Other')], blank=True, null=True),
        ),
    ]
