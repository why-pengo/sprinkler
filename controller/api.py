import sys
import platform
from controller import utils
from scheduler.models import ZoneMap
from _datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from loguru import logger


class ZoneOn(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, zone):
        logger.debug(f"zone = {zone}")
        self.run_for(zone, 5)
        return Response(f'zoneOn: {zone}')

    @staticmethod
    def run_for(zone, minutes):
        zone_map = ZoneMap.objects.get(num__exact=zone)
        bcm = zone_map.bcm
        logger.debug(f"zone = {zone}")
        logger.debug(f"minutes = {minutes}")
        logger.debug(f"BCM = {bcm}")

        # schedule start
        # start_time = datetime.now() + timedelta(seconds=20)
        logger.debug(f"adding relay_call({bcm}, 0) start now")
        utils.relay_call(bcm, 0)
        # scheduler.add_job(relay_call, args=[bcm, 0])

        # schedule stop
        stop_time = datetime.now() + timedelta(minutes=minutes)
        logger.debug("adding relay_call(", zone_map.bcm, ", 1) ", stop_time)
        # scheduler.add_job(relay_call, 'date', run_date=stop_time, args=[bcm, 1])

        return Response(f'runFor: {zone}')


class ZoneOff(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    @staticmethod
    def get(request, zone):
        zone_map = ZoneMap.objects.get(num__exact=zone)
        logger.debug(f"zone = {zone}")
        logger.debug(f"BCM = {zone_map.bcm}")
        utils.relay_call(zone_map.bcm, 1)
        return Response(f'zoneOff: {zone}')


class ListJobs(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    @staticmethod
    def get():
        job_list = []
        # jobs = scheduler.get_jobs()
        jobs = []
        for i in range(0, len(jobs)):
            job = dict()
            job['name'] = jobs[i].name
            args = jobs[i].args
            if len(args) != 0:
                job['arg0'] = args[0]
                job['arg1'] = args[1]
            job['trigger'] = str(jobs[i].trigger)
            logger.debug("found job ", job)
            job_list.append(job)

        return Response(job_list)


class Running(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    @staticmethod
    def get(request, format=None):
        if platform.machine() == 'armv7l':
            import wiringpi

        logger.debug("check if any zone is currently running")
        value = 0
        for zone in ZoneMap.objects.all():
            if 'wiringpi' in sys.modules:
                value = wiringpi.digitalRead(zone.pin)  # Read pin
            else:
                value = 1

            if not value:
                on_off = "On"
                logger.debug("zone = ", zone.num, ", pin = ", zone.pin, " is ", on_off)
                return Response(zone.num)
            else:
                on_off = "Off"

            logger.debug("zone = ", zone.num, ", pin = ", zone.pin, " is ", on_off)

        return Response('none')
