# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-24 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_auto_20170101_0746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image_link',
        ),
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('RG', 'Ring'), ('NK', 'Necklace'), ('BC', 'Bracelet'), ('ER', 'Earrings'), ('UC', 'Unclassified')], default='UC', max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='link',
            field=models.CharField(help_text='Please use Etsy links only', max_length=200),
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
    ]
