# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-06 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paster', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paste',
            name='shortcode',
            field=models.CharField(default=django.utils.timezone.now, max_length=220),
            preserve_default=False,
        ),
    ]