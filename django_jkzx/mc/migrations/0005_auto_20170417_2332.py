# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-17 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mc', '0004_auto_20170417_2305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='os_kernel',
            new_name='os_release',
        ),
    ]