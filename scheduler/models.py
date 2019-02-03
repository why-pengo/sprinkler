from django.db import models


class ZoneMap(models.Model):
    """
    Zone Map
    """
    num = models.IntegerField()
    bcm = models.IntegerField()
    pin = models.IntegerField()
    gpio = models.IntegerField()


