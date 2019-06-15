from django.apps import AppConfig
from loguru import logger


class SchedulerConfig(AppConfig):
    name = 'scheduler'

    def ready(self):
        from controller.utils import init_zone_map, get_current_zone_map, gpio_setup
        from .models import ZoneMap, AppConfig

        logger.debug(f"Checking if zone map is setup.")
        try:
            zone_all = ZoneMap.objects.all()
            if len(zone_all) > 0:
                logger.debug(f"It is already initialized.")
            else:
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
                logger.debug(f"Calling gpio_setup.")
                gpio_setup(zone_map)
            else:
                logger.debug(f"gpio_initialized = {gpio_initialized.value}.")

        except Exception as e:
            logger.debug(f"Exception: {e}")
