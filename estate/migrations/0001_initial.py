# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-07 10:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biz_name', models.CharField(max_length=300)),
                ('email_address', models.EmailField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='businesses/')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('population', models.PositiveIntegerField()),
                ('view_image', models.ImageField(upload_to='neighborhoods/')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='neighborhood_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estate.Neighborhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
