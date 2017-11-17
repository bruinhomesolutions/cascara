# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 00:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.IntegerField()),
                ('data', models.FloatField()),
            ],
        ),
    ]
