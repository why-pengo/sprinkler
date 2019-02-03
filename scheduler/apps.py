from django.apps import AppConfig


class SchedulerConfig(AppConfig):
    name = 'scheduler'

    def ready(self):
        from .utils import init_zone_map, get_current_zone_map, print_zone_map, gpio_setup
        from .models import ZoneMap

        print(f"Checking if zone map is setup.")
        zone_one = ZoneMap.objects.all()
        if len(zone_one) > 0:
            print(f"It is already initialized.")
        else:
            print(f"It is not, initializing zone map.")
            init_zone_map()
        zone_map = get_current_zone_map()
        print_zone_map(zone_map)
        print(f"Calling gpio_setup.")
        gpio_setup(zone_map)
