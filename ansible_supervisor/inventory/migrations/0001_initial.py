# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ansible_alias', models.CharField(max_length=200)),
                ('ansible_host', models.CharField(max_length=200)),
                ('ansible_port', models.PositiveIntegerField(default=22)),
                ('ansible_user', models.CharField(max_length=200)),
            ],
        ),
    ]
