from django.apps import AppConfig


class SchedulerConfig(AppConfig):
    name = 'scheduler'

    def ready(self):
        from controller.utils import init_zone_map, get_current_zone_map, gpio_setup
        from loguru import logger

        logger.debug(f"Checking if zone map is setup.")
        try:
            init_zone_map()
            zone_map = get_current_zone_map()
            gpio_setup(zone_map)
        except Exception as e:
            logger.debug(f"Exception: {e}")
