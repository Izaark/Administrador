# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-16 06:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_projectstatus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectstatus',
            options={'verbose_name_plural': 'ProjectStatus'},
        ),
    ]
