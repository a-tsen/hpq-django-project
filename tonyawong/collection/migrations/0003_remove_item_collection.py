# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 07:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_item_image_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='collection',
        ),
    ]