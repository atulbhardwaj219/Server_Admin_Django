# Generated by Django 2.1.7 on 2020-04-26 08:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instancename', models.CharField(max_length=15)),
                ('ip', models.GenericIPAddressField()),
                ('status', models.CharField(max_length=10)),
                ('request', models.CharField(max_length=10)),
                ('requesttime', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Instancename', models.CharField(max_length=15, unique=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('port', models.PositiveIntegerField(default=22)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('OsType', models.CharField(default='unknown', max_length=50)),
            ],
        ),
    ]