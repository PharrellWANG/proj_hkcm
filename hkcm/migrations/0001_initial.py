# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-30 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cmdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuetime', models.DateTimeField(null=True)),
                ('district', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200)),
                ('crime', models.CharField(max_length=50)),
                ('crimecat', models.CharField(max_length=50)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('title', models.CharField(max_length=500, unique=True)),
                ('URL', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='DistrictsClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_cmdata', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('Districts', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DistrictsForAllLocationsinLocaList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, unique=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('Districts', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HongKongEighteenDistricts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Districts', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='latlngMappingDistricts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_d', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('Districts', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='cmdata',
            unique_together=set([('title', 'crime')]),
        ),
    ]
