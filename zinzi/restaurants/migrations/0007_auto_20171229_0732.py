# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-29 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20171228_0606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='main_image',
            new_name='thumbnail',
        ),
    ]
