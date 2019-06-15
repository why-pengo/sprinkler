import sys
import platform
from scheduler.models import ZoneMap
from datetime import datetime
from loguru import logger
from crontab import CronTab


def gpio_setup(zone_map):
    """set gpio0-7 to output mode and write 0/LOW/OFF
    so we are in a known state at start up"""
    logger.debug(f"entering...")

    logger.debug(f"platform.machine() == {platform.machine()}")
    if platform.machine() == 'armv7l':
        import wiringpi

        if 'wiringpi' in sys.modules:
            logger.debug(f"found wiringpi in sys.modules.")
            wiringpi.wiringPiSetupGpio()  # For GPIO pin numbering
            for i in range(1, len(zone_map) + 1):
                wiringpi.pinMode(zone_map[i].bcm, 1)  # Set pin to 1 ( OUTPUT )
                wiringpi.digitalWrite(zone_map[i].bcm, 1)  # Write (1 = HIGH/OFF, 0 = LOW/ON ) to pin
                logger.debug(f"setting zone = {i} pin/bcm = {zone_map[i].bcm} to OUTPUT/OFF")
        else:
            logger.debug(f"no wiringpi, we in dev?")


def init_zone_map():
    """
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
    # zone 1
    zone_map = ZoneMap()
    zone_map.num = '1'
    zone_map.bcm = '17'
    zone_map.pin = '11'
    zone_map.gpio = '0'
    zone_map.save()

    # zone 2
    zone_map = ZoneMap()
    zone_map.num = '2'
    zone_map.bcm = '18'
    zone_map.pin = '12'
    zone_map.gpio = '1'
    zone_map.save()

    # zone 3
    zone_map = ZoneMap()
    zone_map.num = '3'
    zone_map.bcm = '27'
    zone_map.pin = '13'
    zone_map.gpio = '2'
    zone_map.save()

    # zone 4
    zone_map = ZoneMap()
    zone_map.num = '4'
    zone_map.bcm = '22'
    zone_map.pin = '15'
    zone_map.gpio = '3'
    zone_map.save()

    # zone 5
    zone_map = ZoneMap()
    zone_map.num = '5'
    zone_map.bcm = '23'
    zone_map.pin = '16'
    zone_map.gpio = '4'
    zone_map.save()

    # zone 6
    zone_map = ZoneMap()
    zone_map.num = '6'
    zone_map.bcm = '24'
    zone_map.pin = '18'
    zone_map.gpio = '5'
    zone_map.save()

    # zone 7
    zone_map = ZoneMap()
    zone_map.num = '7'
    zone_map.bcm = '25'
    zone_map.pin = '22'
    zone_map.gpio = '6'
    zone_map.save()

    # zone 8
    zone_map = ZoneMap()
    zone_map.num = '8'
    zone_map.bcm = '4'
    zone_map.pin = '7'
    zone_map.gpio = '7'
    zone_map.save()

    return True


def get_current_zone_map():
    """Query module and return a dict on zone map"""
    zone_map = ZoneMap.objects.all()
    return zone_map


def print_zone_map(zone_map):
    for zone in zone_map:
        logger.debug(f"zone.num = {zone.num}")
        logger.debug(f"\tzone.bcm = {zone.bcm}")
        logger.debug(f"\tzone.pin = {zone.pin}")
        logger.debug(f"\tzone.gpio = {zone.gpio}")


def relay_call(bcm, call):
    """
    Open/Close relay
    0 = On, 1 = Off
    """
    if platform.machine() == 'armv7l':
        import wiringpi

    zone = ZoneMap.objects.get(bcm__exact=int(bcm))
    timestamp = datetime.now()
    logger.debug(f"zone = {zone.num} bcm = {bcm} call = {call} 0/On 1/Off time = {timestamp}")
    if 'wiringpi' in sys.modules:
        value = wiringpi.digitalRead(bcm)  # Read bcm
        logger.debug(f"value before = {value}")
        wiringpi.digitalWrite(bcm, call)  # Write (1 = HIGH/OFF, 0 = LOW/ON ) to pin
        value = wiringpi.digitalRead(bcm)  # Read bcm
        logger.debug(f"value after = {value}")


def read_crontab():
    return CronTab(user=True)


def write_crontab(cron):
    cron.write()


def json_to_crontab_entry():
    pass
