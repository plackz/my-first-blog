# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0004_auto_20170212_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditsections',
            name='section_heading',
            field=models.CharField(max_length=200),
        ),
    ]
