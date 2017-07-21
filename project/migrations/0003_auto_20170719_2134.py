# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170718_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highquality',
            name='quality_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='planning',
            name='planning_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='status',
            name='status_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
