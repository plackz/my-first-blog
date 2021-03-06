# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incidents',
            options={'verbose_name': 'Incidents', 'verbose_name_plural': 'Incidents'},
        ),
        migrations.AddField(
            model_name='incidents',
            name='customer_affected',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incidents',
            name='incident_dt',
            field=models.DateTimeField(verbose_name='incident date'),
        ),
        migrations.AlterField(
            model_name='incidents',
            name='resolution_dt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='completed date'),
        ),
    ]
