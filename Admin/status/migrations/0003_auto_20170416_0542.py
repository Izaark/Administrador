# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-16 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20170416_0502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status'},
        ),
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]