# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [('users', '0011_auto_20161016_1503')]

    operations = [
        migrations.AlterField(model_name='user', name='cache', field=models.OneToOneField(
            blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to='users.UserCache')),
    ]
