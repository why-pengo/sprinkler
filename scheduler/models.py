from django.db import models


class ZoneMap(models.Model):
    """
    Zone Map
    """

    num = models.IntegerField()
    bcm = models.IntegerField()
    pin = models.IntegerField()
    gpio = models.IntegerField()


class ZoneSchedule(models.Model):
    """
    Zone Schedule
    """

    # dow = Day of Week, smtwtfs
    dow = models.CharField(max_length=7)
    start = models.TimeField()
    end = models.TimeField()
    zone = models.IntegerField()
    active = models.BooleanField(default=True)
    run_once = models.BooleanField(default=False)
    crontab = models.CharField(max_length=50)
    cron_key = models.CharField(max_length=15)


class AppConfig(models.Model):
    name = models.CharField(max_length=25, primary_key=True, unique=True)
    value = models.CharField(max_length=25)
