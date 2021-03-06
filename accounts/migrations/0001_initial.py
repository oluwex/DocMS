# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-19 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='username')),
                ('email', models.EmailField(error_messages={'unique': 'A user with the email address already exists.'}, max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(error_messages={'blank': 'First name must be provided.'}, max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(error_messages={'blank': 'Last name must be provided.'}, max_length=255, verbose_name='last name')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
