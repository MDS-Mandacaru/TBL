# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-30 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rankingGroup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupinfo',
            name='ranking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups_info', to='rankingGroup.Ranking'),
        ),
    ]
