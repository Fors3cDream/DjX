# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-25 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20170413_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default='', max_length=100, verbose_name='\u5730\u5740'),
        ),
    ]
