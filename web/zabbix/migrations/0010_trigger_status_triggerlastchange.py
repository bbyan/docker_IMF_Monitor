# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-31 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zabbix', '0009_auto_20180531_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger_status',
            name='triggerlastchange',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
