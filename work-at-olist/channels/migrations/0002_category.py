# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channels.Channel')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='channels.Category')),
            ],
        ),
    ]
