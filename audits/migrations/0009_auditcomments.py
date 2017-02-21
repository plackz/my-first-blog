# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 02:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0008_auto_20170213_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditor_name', models.CharField(max_length=200)),
                ('finding', models.CharField(choices=[('Y', 'Yes'), ('N', 'No'), ('O', 'Obs')], max_length=1)),
                ('sap_ref', models.CharField(max_length=20, verbose_name='SAP REF')),
                ('question_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='audits.AuditQuestions')),
            ],
        ),
    ]