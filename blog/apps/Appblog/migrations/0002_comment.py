# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 03:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechacreacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
                ('idEntrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appblog.Entrada')),
            ],
        ),
    ]