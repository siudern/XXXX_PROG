# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-19 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mc', '0006_auto_20170419_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='cpu_model',
            field=models.CharField(max_length=128, verbose_name='CPU\u578b\u53f7'),
        ),
        migrations.AlterField(
            model_name='cpu',
            name='update_data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='nic',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ram',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
