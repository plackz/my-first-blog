# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0005_auto_20170213_0741'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditQuestions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False, verbose_name='question id')),
                ('subsection_num', models.CharField(max_length=20, verbose_name='sub-section no.')),
                ('section_text', models.CharField(max_length=200, verbose_name='section')),
                ('subsection_text', models.CharField(max_length=200, verbose_name='sub-section')),
                ('general_question', models.TextField()),
                ('audit_specific', models.TextField(verbose_name='audit specific question')),
                ('audit_guidance', models.TextField(verbose_name='audit guide')),
                ('section_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audits.AuditSections')),
            ],
            options={
                'verbose_name': 'Audit Question',
                'verbose_name_plural': 'Audit Questions',
            },
        ),
    ]
