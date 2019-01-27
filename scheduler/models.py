from django.db import models


class zone(models.Model):
    """Zone Map"""
    num = models.IntegerField()
    pin = models.IntegerField()
    bcm = models.IntegerField()
    gpio = models.IntegerField()
    # map zone number to BCM number
    #              BCM   pin
    # zoneMap[1] = 17  # 11 gpio0
    # zoneMap[2] = 18  # 12 gpio1
    # zoneMap[3] = 27  # 13 gpio2
    # zoneMap[4] = 22  # 15 gpio3
    # zoneMap[5] = 23  # 16 gpio4
    # zoneMap[6] = 24  # 18 gpio5
    # zoneMap[7] = 25  # 22 gpio6
    # zoneMap[8] = 4   # 7 gpio7

