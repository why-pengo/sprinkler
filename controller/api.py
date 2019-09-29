import sys
import platform
from controller import utils
from scheduler.models import ZoneMap, ZoneSchedule
from _datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from loguru import logger
from django.conf import settings
from controller import utils


class ZoneOn(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    tz = settings.TIME_ZONE

    def get(self, request, zone):
        logger.debug(f"zone = {zone}")
        timestamp = f"{datetime.now().strftime('%X')} {self.tz}"
        self.run_for(zone, 5)
        rv = {
            'zoneOn': f"{zone}",
            'timestamp': f"{timestamp}"
        }
        # return Response(f'zoneOn: {zone}, timestamp: {timestamp}')
        return Response(rv)

    @staticmethod
    def run_for(zone, minutes):
        zone_map = ZoneMap.objects.get(num__exact=zone)
        bcm = zone_map.bcm
        logger.debug(f"zone = {zone}")
        # logger.debug(f"minutes = {minutes}")
        logger.debug(f"BCM = {bcm}")

        # schedule start
        # start_time = datetime.now() + timedelta(seconds=20)
        # logger.debug(f"adding relay_call({bcm}, 0) start now")
        timestamp = datetime.now().strftime("%X")
        utils.relay_call(bcm, 0)
        # scheduler.add_job(relay_call, args=[bcm, 0])

        # schedule stop
        # stop_time = datetime.now() + timedelta(minutes=minutes)
        # logger.debug(f"adding relay_call({zone_map.bcm}, 1)")
        # scheduler.add_job(relay_call, 'date', run_date=stop_time, args=[bcm, 1])

        return Response(f'runFor: {zone}, timestamp: {timestamp}')


class ZoneOff(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    tz = settings.TIME_ZONE

    def get(self, request, zone):
        zone_map = ZoneMap.objects.get(num__exact=zone)
        timestamp = f"{datetime.now().strftime('%X')} {self.tz}"
        bcm = zone_map.bcm
        logger.debug(f"zone = {zone}")
        logger.debug(f"BCM = {bcm}")
        # TODO: add timestamp
        utils.relay_call(bcm, 1)
        rv = {
            'zoneOff': f"{zone}",
            'timestamp': f"{timestamp}"
        }
        # return Response(f'zoneOff: {zone}')
        return Response(rv)


class ListJobs(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    @staticmethod
    def get(request):
        zone_list = ZoneMap.objects.order_by('num')
        job_list = list()
        for zone in zone_list:
            schedule = ZoneSchedule.objects.filter(zone__exact=zone.num)
            if len(schedule) > 0:
                zs_list = list()
                for s in schedule:
                    zs_dict = dict()
                    zs_dict['dow'] = s.dow
                    zs_dict['start'] = s.start
                    zs_dict['end'] = s.end
                    zs_dict['active'] = s.active
                    zs_list.append(zs_dict)
                job_dict = dict()
                job_dict[zone.num] = zs_list
                job_list.append(job_dict)

        return Response(job_list)


class Running(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    @staticmethod
    def get(request, format=None):
        return Response(utils.whats_running())
