# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-03 16:30
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
