# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 06:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20171220_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='thumbnail',
            new_name='main_image',
        ),
    ]