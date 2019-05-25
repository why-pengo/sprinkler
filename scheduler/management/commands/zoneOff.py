from django.core.management.base import BaseCommand
from scheduler.models import ZoneMap
from controller.utils import relay_call


class Command(BaseCommand):
    help = 'Turns off the requested zone.'

    def add_arguments(self, parser):
        parser.add_argument('zone', type=str)

    def handle(self, *args, **options):
        zone = options['zone']
        zone_map = ZoneMap.objects.get(num__exact=zone)
        self.log(f"scheduler/management/commands/zoneOff: zone = {zone}")
        self.log(f"scheduler/management/commands/zoneOff: BCM = {zone_map.bcm}")
        relay_call(zone_map.bcm, 0)

    def log(self, msg):
        self.stdout.write(self.style.SUCCESS(msg))
