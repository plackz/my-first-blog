# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('standard_work', '0002_auto_20170212_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkGuidance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkRemarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark_text', models.TextField()),
                ('remark_guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standard_work.WorkGuidance')),
            ],
        ),
        migrations.AlterField(
            model_name='standardwork',
            name='work_title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='workremarks',
            name='remark_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standard_work.StandardWork'),
        ),
        migrations.AddField(
            model_name='workguidance',
            name='guide_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='standard_work.StandardWork'),
        ),
    ]
