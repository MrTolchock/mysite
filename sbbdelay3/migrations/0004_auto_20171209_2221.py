# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbbdelay3', '0003_auto_20171209_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='ab_delay',
            field=models.CharField(max_length=20),
        ),
    ]
