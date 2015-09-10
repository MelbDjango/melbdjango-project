# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20150909_0540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonenumber',
            old_name='phone_number',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='phonenumber',
            name='phone_type',
        ),
        migrations.AddField(
            model_name='email',
            name='type',
            field=models.CharField(null=True, max_length=16, choices=[(None, 'Unspecified'), ('Home', 'Home'), ('Work', 'Work'), ('Campus', 'Campus'), ('Dormitory', 'Dormitory'), ('Other', 'Other')]),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='phone',
            field=models.CharField(null=True, max_length=16, choices=[(None, 'Unspecified'), ('Home', 'Home'), ('Work', 'Work'), ('Campus', 'Campus'), ('Dormitory', 'Dormitory'), ('Other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='address',
            name='type',
            field=models.CharField(null=True, max_length=16, choices=[(None, 'Unspecified'), ('Home', 'Home'), ('Work', 'Work'), ('Main', 'Main'), ('Branch', 'Branch'), ('Mailing', 'Mail'), ('Billing', 'Billing'), ('Legal', 'Legal'), ('Campus', 'Campus'), ('Dormitory', 'Dormitory'), ('Other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(null=True, max_length=16, choices=[(None, 'None'), ('Mr.', 'Mr'), ('Miss', 'Miss'), ('Ms.', 'Ms'), ('Mrs.', 'Mrs'), ('Dr.', 'Dr'), ('Prof.', 'Prof'), ('Rev.', 'Rev'), ('Lt.', 'Lt'), ('Cpt.', 'Cpt'), ('Maj.', 'Maj'), ('Gen.', 'Gen'), ('Esq', 'Esq'), ('Sr.', 'Sr'), ('Jr.', 'Jr'), ('Hon.', 'Hon'), ('Rt. Hon.', 'Rt Hon')], blank=True),
        ),
    ]
