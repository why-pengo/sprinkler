import sys
import platform
import controller.settings as settings
from scheduler.models import ZoneMap, ZoneSchedule
from datetime import datetime
from loguru import logger
from crontab import CronTab


def gpio_setup(zone_map):
    """For gpio0-7 write 0/LOW/OFF so we are in a known state at start up"""
    logger.debug("entering...")
    logger.debug(f"platform.machine() == {platform.machine()}")
    if platform.machine() == "armv7l":
        import gpiozero
        import gpiozero.pins.rpigpio

        gpiozero.pins.rpigpio.RPiGPIOPin.close = close

        if "gpiozero" in sys.modules:
            logger.debug("found gpiozero in sys.modules.")
            for i in range(1, len(zone_map)):
                # (1 = HIGH/OFF, 0 = LOW/ON ) for our relay board
                bcm = int(zone_map[i].bcm)
                relay = gpiozero.OutputDevice(
                    pin=bcm,
                    pin_factory=gpiozero.pins.rpigpio.RPiGPIOFactory(),
                    initial_value=None,
                    active_high=False,
                )
                value = relay.value
                logger.debug(f"bcm value = {value}")
                relay.off()
                logger.debug(
                    f"setting zone = {i} pin/bcm = {zone_map[i].bcm} to OUTPUT/OFF"
                )
                logger.debug(f"bcm value = {value}")
        else:
            logger.debug("no gpiozero")


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
    # print(f"count = {ZoneMap.objects.count()}")
    if ZoneMap.objects.count() != 0:
        return True

    # zone 1
    zone_map = ZoneMap()
    zone_map.num = "1"
    zone_map.bcm = "17"
    zone_map.pin = "11"
    zone_map.gpio = "0"
    zone_map.save()

    # zone 2
    zone_map = ZoneMap()
    zone_map.num = "2"
    zone_map.bcm = "18"
    zone_map.pin = "12"
    zone_map.gpio = "1"
    zone_map.save()

    # zone 3
    zone_map = ZoneMap()
    zone_map.num = "3"
    zone_map.bcm = "27"
    zone_map.pin = "13"
    zone_map.gpio = "2"
    zone_map.save()

    # zone 4
    zone_map = ZoneMap()
    zone_map.num = "4"
    zone_map.bcm = "22"
    zone_map.pin = "15"
    zone_map.gpio = "3"
    zone_map.save()

    # zone 5
    zone_map = ZoneMap()
    zone_map.num = "5"
    zone_map.bcm = "23"
    zone_map.pin = "16"
    zone_map.gpio = "4"
    zone_map.save()

    # zone 6
    zone_map = ZoneMap()
    zone_map.num = "6"
    zone_map.bcm = "24"
    zone_map.pin = "18"
    zone_map.gpio = "5"
    zone_map.save()

    # zone 7
    zone_map = ZoneMap()
    zone_map.num = "7"
    zone_map.bcm = "25"
    zone_map.pin = "22"
    zone_map.gpio = "6"
    zone_map.save()

    # zone 8
    zone_map = ZoneMap()
    zone_map.num = "8"
    zone_map.bcm = "4"
    zone_map.pin = "7"
    zone_map.gpio = "7"
    zone_map.save()

    return True


def get_current_zone_map():
    """Query module and return a dict on zone map"""
    zone_map = ZoneMap.objects.all()
    return zone_map


def print_zone_map():
    zone_map = get_current_zone_map()
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
    if platform.machine() == "armv7l":
        import gpiozero
        import gpiozero.pins.rpigpio

        gpiozero.pins.rpigpio.RPiGPIOPin.close = close

        bcm = int(bcm)
        zone = ZoneMap.objects.get(bcm__exact=bcm)
        timestamp = datetime.now()
        logger.debug(
            f"zone = {zone.num} bcm = {bcm} call = {call} # 0/On 1/Off time = {timestamp}"
        )
        if "gpiozero" in sys.modules:
            # (1 = HIGH/OFF, 0 = LOW/ON ) for our relay board
            relay = gpiozero.OutputDevice(
                pin=bcm,
                initial_value=None,
                pin_factory=gpiozero.pins.rpigpio.RPiGPIOFactory(),
                active_high=False,
            )
            if call == 0:
                relay.on()
            else:
                relay.off()
            value = relay.value
            logger.debug(f"value after = {value}")


def read_crontab():
    return CronTab(user=True)


def save_crontab_entry(zs_id):
    logger.debug(f"zs_id = {zs_id}")
    zone_obj = ZoneSchedule.objects.get(pk=zs_id)
    dow = str(zone_obj.dow)
    logger.debug(f"dow = {dow}")
    comment_id = f"{datetime.now().isoformat(timespec='minutes')}-{dow}"
    zone_obj.cron_key = comment_id
    zone_obj.save()

    zone = zone_obj.zone
    start = zone_obj.start
    s_hour, s_min, s_secs = str(start).split(":", 3)
    logger.debug(f"s_hour = {s_hour}, s_min = {s_min}, s_secs = {s_secs}")

    end = zone_obj.end
    e_hour, e_min, e_secs = str(end).split(":", 3)
    logger.debug(f"e_hour = {e_hour}, e_min = {e_min}, e_secs = {e_secs}")

    cron = read_crontab()

    # get Django root
    base_dir = settings.BASE_DIR

    start_job = cron.new(
        command=f"{base_dir}/scripts/cron_run.sh {base_dir} {zone} on",
        comment=f"{comment_id}",
    )
    start_job.dow.on(dow)
    start_job.hour.on(s_hour)
    start_job.minute.on(s_min)
    logger.debug(f"start_job.is_valid = {start_job.is_valid()}")

    end_job = cron.new(
        command=f"{base_dir}/scripts/cron_run.sh {base_dir} {zone} off",
        comment=f"{comment_id}",
    )
    end_job.dow.on(dow)
    end_job.hour.on(e_hour)
    end_job.minute.on(e_min)
    logger.debug(f"end_job.is_valid = {end_job.is_valid()}")

    cron.write()

    for line in cron.lines:
        logger.debug(f"cron entry: {line}")

    # TODO: if run_once is True delete job after it stops.


def delete_crontab_entry(zs_id):
    zone_obj = ZoneSchedule.objects.get(pk=zs_id)
    comment_id = zone_obj.cron_key
    zone_obj.delete()

    cron = read_crontab()

    for line in cron.lines:
        logger.debug(f"cron entry: {line}")

    iter = cron.find_comment(f"{comment_id}")

    for line in iter:
        logger.debug(f"found {line}")

    logger.debug(f"deleting schedule id = {zs_id}, comment_id = {comment_id}")
    cron.remove_all(comment=f"{comment_id}")
    cron.write()


def whats_running():
    if platform.machine() == "armv7l":
        import gpiozero
        import gpiozero.pins.rpigpio

        gpiozero.pins.rpigpio.RPiGPIOPin.close = close

    logger.debug("check if any zone is currently running")
    value = 1  # local debugging
    # (1 = HIGH/OFF, 0 = LOW/ON )
    for zone in ZoneMap.objects.all():
        bcm = int(zone.bcm)
        if "gpiozero" in sys.modules:
            relay = gpiozero.OutputDevice(
                pin=bcm,
                initial_value=None,
                pin_factory=gpiozero.pins.rpigpio.RPiGPIOFactory(),
            )
            value = relay.value
            logger.debug(f"digitalRead returned = {value}")

        if value == 0:
            on_off = "On"
            logger.debug(f"zone {zone.num} is {on_off}")
            return zone.num
        else:
            on_off = "Off"

        logger.debug(f"zone {zone.num} is {on_off}")

    return 0


def dow_to_day(dow):
    if dow == "0" or dow == "7":
        return "Sun"
    if dow == "1":
        return "Mon"
    if dow == "2":
        return "Tue"
    if dow == "3":
        return "Wed"
    if dow == "4":
        return "Thu"
    if dow == "5":
        return "Fri"
    if dow == "6":
        return "Sat"


def close(self):
    """This function is a workaround for gpiozero's cleanup on close resetting pins state"""
    # https://github.com/gpiozero/gpiozero/issues/707
    pass
