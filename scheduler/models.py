from django.db import models


class ZoneMap(models.Model):
    """
    Zone Map
           zone  BCM  pin gpio
    zoneMap[1] = 17  # 11 gpio0
    zoneMap[2] = 18  # 12 gpio1
    zoneMap[3] = 27  # 13 gpio2
    zoneMap[4] = 22  # 15 gpio3
    zoneMap[5] = 23  # 16 gpio4
    zoneMap[6] = 24  # 18 gpio5
    zoneMap[7] = 25  # 22 gpio6
    zoneMap[8] = 4   # 7 gpio7
    """
    num = models.IntegerField()
    bcm = models.IntegerField()
    pin = models.IntegerField()
    gpio = models.IntegerField()

