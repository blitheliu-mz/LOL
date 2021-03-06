# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-02 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applications',
            options={'verbose_name': '\u7cfb\u7edf\u53d1\u5e03-\u5e94\u7528', 'verbose_name_plural': '\u7cfb\u7edf\u53d1\u5e03-\u5e94\u7528'},
        ),
        migrations.AlterModelOptions(
            name='environment',
            options={'verbose_name': '\u7cfb\u7edf\u53d1\u5e03-\u73af\u5883', 'verbose_name_plural': '\u7cfb\u7edf\u53d1\u5e03-\u73af\u5883'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': '\u7cfb\u7edf\u53d1\u5e03-\u9879\u76ee', 'verbose_name_plural': '\u7cfb\u7edf\u53d1\u5e03-\u9879\u76ee'},
        ),
        migrations.AlterField(
            model_name='projects',
            name='Applications',
            field=models.ManyToManyField(blank=True, null=True, to='projectdata.Applications', verbose_name='\u5e94\u7528\u5173\u8054'),
        ),
    ]
