# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snippet',
            new_name='Project',
        ),
    ]
