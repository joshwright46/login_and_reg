# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-26 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]
