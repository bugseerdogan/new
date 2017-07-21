# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-18 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HighQuality',
            fields=[
                ('quality_id', models.DecimalField(decimal_places=0, max_digits=22, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('planning_id', models.DecimalField(decimal_places=0, max_digits=22, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('planned_date', models.DateTimeField()),
                ('bl', models.CharField(max_length=100)),
                ('applied_date', models.DateTimeField()),
                ('notes', models.CharField(max_length=250)),
                ('is_AL', models.BooleanField(default=False)),
                ('is_BL', models.BooleanField(default=False)),
                ('quality', models.ForeignKey(db_column='quality_id', on_delete=django.db.models.deletion.CASCADE, to='project.HighQuality')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('publication_id', models.DecimalField(decimal_places=0, max_digits=22, primary_key=True, serialize=False)),
                ('publication_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.DecimalField(decimal_places=0, max_digits=22, primary_key=True, serialize=False)),
                ('status_text', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='planning',
            name='status',
            field=models.ForeignKey(db_column='status_id', on_delete=django.db.models.deletion.CASCADE, to='project.Status'),
        ),
        migrations.AddField(
            model_name='planning',
            name='type',
            field=models.ForeignKey(db_column='publication_id', on_delete=django.db.models.deletion.CASCADE, to='project.Publication'),
        ),
    ]
