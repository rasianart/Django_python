# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='snippet',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
