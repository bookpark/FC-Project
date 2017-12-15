# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_reservationcancel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCancel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=50)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reservations.Payment')),
            ],
        ),
        migrations.RemoveField(
            model_name='reservationcancel',
            name='payment',
        ),
        migrations.DeleteModel(
            name='ReservationCancel',
        ),
    ]