# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-03 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oidc_provider', '0026_client_multiple_response_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='_amr',
            field=models.CharField(max_length=255, null=True, verbose_name='Authentication Method Reference'),
        ),
        migrations.AddField(
            model_name='code',
            name='acr',
            field=models.CharField(max_length=255, null=True, verbose_name='Authentication Context Reference'),
        ),
    ]
