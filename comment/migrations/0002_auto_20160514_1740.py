# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-05-14 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentinfo',
            name='comment_news_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='commentinfo',
            name='comment_news_title',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='commentinfo',
            name='comment_news_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
