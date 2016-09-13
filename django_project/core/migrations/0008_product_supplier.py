# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Supplier'),
            preserve_default=False,
        ),
    ]