# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-26 07:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staffuser',
            options={'permissions': (('add_address', 'Can add address'), ('change_address', 'Can change address'), ('delete_address', 'Can delete address')), 'verbose_name': 'staff'},
        ),
    ]
