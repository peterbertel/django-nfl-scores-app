# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-08 22:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(default=1)),
                ('home_score', models.IntegerField(default=0)),
                ('home_points_q1', models.IntegerField(default=0)),
                ('home_points_q2', models.IntegerField(default=0)),
                ('home_points_q3', models.IntegerField(default=0)),
                ('home_points_q4', models.IntegerField(default=0)),
                ('away_score', models.IntegerField(default=0)),
                ('away_points_q1', models.IntegerField(default=0)),
                ('away_points_q2', models.IntegerField(default=0)),
                ('away_points_q3', models.IntegerField(default=0)),
                ('away_points_q4', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=50, unique=True)),
                ('long_name', models.CharField(max_length=200, unique=True)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='nfl_scores.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='nfl_scores.Team'),
        ),
    ]
