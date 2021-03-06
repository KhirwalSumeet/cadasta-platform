# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-25 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicalquestionnaire',
            old_name='name',
            new_name='filename',
        ),
        migrations.RenameField(
            model_name='questionnaire',
            old_name='name',
            new_name='filename',
        ),
        migrations.AlterField(
            model_name='historicalquestionnaire',
            name='version',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='version',
            field=models.BigIntegerField(default=1),
        ),
    ]
