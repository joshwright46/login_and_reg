# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-31 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_delete_login'),
        ('wall_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='wall_app.Comment')),
                ('messages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='wall_app.Message')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='login.User')),
            ],
        ),
    ]
