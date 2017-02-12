# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0003_audittype_type_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auditsections',
            options={'verbose_name': 'Audit section', 'verbose_name_plural': 'Audit sections'},
        ),
        migrations.RenameField(
            model_name='auditsections',
            old_name='audit_type_section',
            new_name='audit_type',
        ),
        migrations.RemoveField(
            model_name='audittype',
            name='audit_type',
        ),
        migrations.AddField(
            model_name='audittype',
            name='audit_type_fld',
            field=models.CharField(choices=[('ISO', 'ISO 9001'), ('API', 'API 6D and 6A'), ('PED', 'PED'), ('DNV', 'DNV'), ('EAC', 'Russian Certification'), ('ABS', 'ABS'), ('Cust', 'Customer audit')], default='default', max_length=4, verbose_name='audit type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audittype',
            name='audit_regulation',
            field=models.CharField(choices=[('ISO', 'ISO 9001:2015'), ('API', 'API 6D, 6A, Q1, 607'), ('PED', 'EU 2014/68'), ('Cust', 'Customer specification'), ('TBD', 'To be determined')], max_length=4),
        ),
    ]
