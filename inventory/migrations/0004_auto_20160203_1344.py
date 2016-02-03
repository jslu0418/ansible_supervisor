# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 13:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20160203_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='ansible_group',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='host',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 3, 13, 44, 50, 38197, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
