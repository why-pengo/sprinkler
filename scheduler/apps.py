from django.apps import AppConfig
from loguru import logger


class SchedulerConfig(AppConfig):
    name = 'scheduler'

    def ready(self):
        from controller.utils import init_zone_map, get_current_zone_map, gpio_setup
        from .models import ZoneMap, AppConfig

        # print(f"scheduler/apps::ready: Checking if zone map is setup.")
        logger.debug(f"scheduler/apps::ready: Checking if zone map is setup.")
        try:
            zone_all = ZoneMap.objects.all()
            if len(zone_all) > 0:
                # print(f"scheduler/apps::ready: It is already initialized.")
                logger.debug(f"It is already initialized.")
            else:
                # print(f"scheduler/apps::ready: It is not, initializing zone map.")
                logger(f"It is not, initializing zone map.")
                init_zone_map()
            zone_map = get_current_zone_map()
            # print_zone_map(zone_map)

            try:
                gpio_initialized = AppConfig.objects.get(name='gpio_initialized')
            except AppConfig.DoesNotExist:
                gpio_initialized = 'False'
            if gpio_initialized is 'False':
                gpio_initialized = AppConfig(name='gpio_initialized', value='True')
                gpio_initialized.save()
                # print(f"scheduler/apps::ready: Calling gpio_setup.")
                logger.debug(f"Calling gpio_setup.")
                gpio_setup(zone_map)
            else:
                # print(f"scheduler/apps::ready: gpio_initialized = {gpio_initialized.value}.")
                logger.debug(f"gpio_initialized = {gpio_initialized.value}.")

        except Exception as e:
            # print(f"scheduler/apps::ready: Exception: {e}")
            logger.debug(f"scheduler/apps::ready: Exception: {e}")
