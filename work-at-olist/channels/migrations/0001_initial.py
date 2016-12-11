# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, serialize=False)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]
