from django.core.management.base import BaseCommand
from scheduler.models import ZoneMap
from controller.utils import relay_call


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('zone', type=str, help='Zone by number.')
        parser.add_argument('on_off', type=str, help='Turn on or off the requested zone.')

    def handle(self, *args, **options):
        zone = options['zone']
        on_off = options['on_off']
        zone_map = ZoneMap.objects.get(num__exact=zone)
        self.log(f"scheduler/management/commands/zoneOnOff: zone = {zone}")
        self.log(f"scheduler/management/commands/zoneOnOff: BCM = {zone_map.bcm}")
        if on_off == 'on':
            self.log(f"scheduler/management/commands/zoneOnOff: turning on, on_off = {on_off}")
            relay_call(zone_map.bcm, 0)
        else:
            self.log(f"scheduler/management/commands/zoneOnOff: turning off, on_off = {on_off}")
            relay_call(zone_map.bcm, 1)

    def log(self, msg):
        self.stdout.write(self.style.SUCCESS(msg))
