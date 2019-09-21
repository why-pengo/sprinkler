# Generated by Django 2.2.5 on 2019-09-21 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppConfig',
            fields=[
                ('name', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('value', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='ZoneMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('bcm', models.IntegerField()),
                ('pin', models.IntegerField()),
                ('gpio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ZoneSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dow', models.CharField(max_length=7)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('zone', models.IntegerField()),
                ('active', models.BooleanField()),
                ('crontab', models.CharField(max_length=50)),
                ('cron_key', models.CharField(max_length=15)),
            ],
        ),
    ]
