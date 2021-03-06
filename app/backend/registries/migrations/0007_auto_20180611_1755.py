# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registries', '0006_auto_20180608_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='registriesapplication',
            name='removal_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registriesapplication',
            name='removal_reason',
            field=models.ForeignKey(blank=True, db_column='registries_removal_reason_code', null=True, on_delete=django.db.models.deletion.PROTECT, to='registries.RegistriesRemovalReason', verbose_name='Removal Reason'),
        ),
    ]
