from django.apps import AppConfig


class SchedulerConfig(AppConfig):
    name = 'scheduler'

    def ready(self):
        from .utils import init_zone_map, get_current_zone_map, print_zone_map, gpio_setup
        from .models import ZoneMap

        print(f"apps::ready: Checking if zone map is setup.")
        try:
            zone_all = ZoneMap.objects.all()
            if len(zone_all) > 0:
                print(f"apps::ready: It is already initialized.")
            else:
                print(f"apps::ready: It is not, initializing zone map.")
                init_zone_map()
            zone_map = get_current_zone_map()
            # print_zone_map(zone_map)
            print(f"apps::ready: Calling gpio_setup.")
            gpio_setup(zone_map)
        except Exception as e:
            print(f"apps::ready: Exception: {e}")
