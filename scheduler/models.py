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
    active = models.BooleanField()

