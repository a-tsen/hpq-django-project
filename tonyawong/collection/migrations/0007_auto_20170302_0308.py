# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-02 03:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0006_auto_20170124_0034'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('rings', 'Ring'), ('necklaces', 'Necklace'), ('bracelets', 'Bracelet'), ('earrings', 'Earrings'), ('miscellaneous', 'Miscellaneous')], default='miscellaneous', max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='link',
            field=models.CharField(help_text='Please use Etsy links only', max_length=200, validators=[django.core.validators.RegexValidator(code='Invalid key', message='Must be an Etsy item link', regex='^https://www.etsy.com/uk/listing/[0-9]+(\\/[a-z\\-]+)?$')]),
        ),
    ]