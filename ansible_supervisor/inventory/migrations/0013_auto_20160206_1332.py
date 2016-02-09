# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20160206_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='ansible_children',
            field=models.ManyToManyField(blank=True, to='inventory.Group'),
        ),
        migrations.AlterField(
            model_name='group',
            name='ansible_hosts',
            field=models.ManyToManyField(to='inventory.Host'),
        ),
    ]