# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='image',
            field=models.FileField(default=b'noimage.png', upload_to=b'images/'),
        ),
    ]
