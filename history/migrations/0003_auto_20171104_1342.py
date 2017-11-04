# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-04 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_auto_20171104_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hurricane',
            name='points',
        ),
        migrations.AddField(
            model_name='hurricanepoint',
            name='parent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='history.Hurricane'),
        ),
    ]