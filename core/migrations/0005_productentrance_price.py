# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20160829_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='productentrance',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]