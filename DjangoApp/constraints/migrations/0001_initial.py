# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-02 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entries_ion_frac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dictionary_tag', models.TextField()),
                ('reference', models.TextField()),
                ('description', models.TextField()),
                ('redshift', models.FloatField()),
                ('ion_frac', models.FloatField()),
                ('err_up', models.FloatField(null=True)),
                ('err_down', models.FloatField(null=True)),
                ('err_up2', models.FloatField(null=True)),
                ('err_down2', models.FloatField(null=True)),
                ('upper_lim', models.BooleanField()),
                ('lower_lim', models.BooleanField()),
            ],
        ),
    ]
