# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 01:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yj_logs', '0002_auto_20170601_0908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name_plural': '主题'},
        ),
    ]