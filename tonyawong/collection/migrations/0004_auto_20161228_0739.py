# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_remove_item_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_link',
            field=models.CharField(max_length=200),
        ),
    ]
