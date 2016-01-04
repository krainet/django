# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-04 08:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 4, 8, 12, 25, 227771)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userdetail',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 1, 4, 8, 12, 33, 57779)),
            preserve_default=False,
        ),
    ]
