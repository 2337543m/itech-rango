# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-01-23 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20180122_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='hello'),
            preserve_default=False,
        ),
    ]
