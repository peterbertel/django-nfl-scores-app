# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-21 16:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfl_scores', '0003_auto_20161119_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='tied_game',
        ),
    ]