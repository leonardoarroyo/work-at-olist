# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-06 00:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0004_auto_20161204_1604'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('name', 'parent', 'channel')]),
        ),
    ]
