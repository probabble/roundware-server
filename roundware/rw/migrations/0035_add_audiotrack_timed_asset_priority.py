# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-15 19:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rw', '0034_add_asset_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiotrack',
            name='timed_asset_priority',
            field=models.CharField(choices=[('highest', 'highest'), ('normal', 'normal'), ('lowest', 'lowest'), ('discard', 'discard')], default='normal', max_length=10, verbose_name='Timed Asset Priority'),
        ),
    ]
