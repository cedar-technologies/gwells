# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-23 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gwells', '0042_auto_20171123_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='alteration_end_date',
            field=models.DateTimeField(null=True, verbose_name='Alteration Date'),
        ),
        migrations.AlterField(
            model_name='well',
            name='construction_end_date',
            field=models.DateTimeField(null=True, verbose_name='Construction Date'),
        ),
        migrations.AlterField(
            model_name='well',
            name='decommission_end_date',
            field=models.DateTimeField(null=True, verbose_name='Decommission Date'),
        ),
    ]
