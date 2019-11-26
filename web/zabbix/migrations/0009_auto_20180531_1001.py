# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-31 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zabbix', '0008_auto_20180530_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger_status',
            name='triggercomment',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='trigger_status',
            name='triggerpriority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]