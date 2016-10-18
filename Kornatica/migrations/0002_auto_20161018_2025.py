# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-18 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kornatica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstanceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Abbr', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.CharField(max_length=1000)),
                ('LanguageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kornatica.Language')),
                ('Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kornatica.InstanceType')),
            ],
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='Description',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='Name',
        ),
        migrations.AddField(
            model_name='rooms',
            name='DistanceFromCenter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rooms',
            name='DistanceFromSee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rooms',
            name='NumberOfSeats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rooms',
            name='Parking',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='rooms',
            name='Pets',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='rooms',
            name='Satellite',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='rooms',
            name='TV',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='rooms',
            name='WiFi',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='rooms',
            name='DescriptionTranslationId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Description', to='Kornatica.Translation'),
        ),
        migrations.AddField(
            model_name='rooms',
            name='NameTranslationId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Name', to='Kornatica.Translation'),
        ),
    ]
