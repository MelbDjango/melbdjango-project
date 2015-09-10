# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('type', models.IntegerField(default=0)),
                ('title', models.TextField(blank=True)),
                ('address_1', models.TextField()),
                ('address_2', models.TextField(blank=True)),
                ('contact_name', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('title', 'address_1', 'address_2'),
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('nick', models.CharField(null=True, max_length=64, blank=True)),
                ('company', models.BooleanField(default=False)),
                ('title', models.CharField(null=True, max_length=16, blank=True)),
                ('addresses', models.ManyToManyField(to='contacts.Address')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('abbrev', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('postcode', models.CharField(max_length=8)),
            ],
            options={
                'ordering': ('name', 'state'),
                'verbose_name_plural': 'localities',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=32)),
                ('phone_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('abbrev', models.CharField(max_length=6)),
                ('country', models.ForeignKey(to='contacts.Country')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='locality',
            name='state',
            field=models.ForeignKey(to='contacts.State'),
        ),
        migrations.AddField(
            model_name='contact',
            name='emails',
            field=models.ManyToManyField(to='contacts.Email'),
        ),
        migrations.AddField(
            model_name='address',
            name='locality',
            field=models.ForeignKey(to='contacts.Locality'),
        ),
    ]
