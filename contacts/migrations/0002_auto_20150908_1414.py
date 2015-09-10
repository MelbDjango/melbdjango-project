# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_1',
            field=models.CharField(max_length=1022),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_2',
            field=models.CharField(max_length=1022, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='contact_name',
            field=models.TextField(max_length=1022, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='title',
            field=models.CharField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(choices=[(None, 'None'), ('Mr.', 'MR'), ('Miss', 'MISS'), ('Ms.', 'MS'), ('Mrs.', 'MRS'), ('Dr.', 'DR'), ('Prof.', 'PROF'), ('Rev.', 'REV'), ('Lt.', 'LT'), ('Cpt.', 'CPT'), ('Maj.', 'MAJ'), ('Gen.', 'GEN'), ('Esq', 'ESQ'), ('Sr.', 'SR'), ('Jr.', 'JR'), ('Hon.', 'HON'), ('Rt. Hon.', 'RT HON')], max_length=16, null=True, blank=True),
        ),
    ]
