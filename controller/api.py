"""REST API"""
from datetime import datetime
from django.conf import settings
from loguru import logger
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from controller import utils
from scheduler.models import ZoneMap, ZoneSchedule


class ZoneOn(APIView):
    """Run a zone"""

    permission_classes = (permissions.IsAuthenticated,)
    tz = settings.TIME_ZONE

    def put(self, request, zone):
        logger.debug(f"zone = {zone}")
        zone_map = ZoneMap.objects.get(num__exact=zone)
        timestamp = f"{datetime.now().strftime('%X')} {self.tz}"
        bcm = zone_map.bcm
        logger.debug(f"bcm = {bcm}")
        utils.relay_call(bcm, 0)
        rv = {"zoneOn": f"{zone}", "timestamp": f"{timestamp}"}
        logger.info(f"rv = {rv}")
        return Response(rv)


class ZoneOff(APIView):
    """Stop a zone"""

    permission_classes = (permissions.IsAuthenticated,)
    tz = settings.TIME_ZONE

    def put(self, request, zone):
        zone_map = ZoneMap.objects.get(num__exact=zone)
        timestamp = f"{datetime.now().strftime('%X')} {self.tz}"
        bcm = zone_map.bcm
        logger.debug(f"zone = {zone}")
        logger.debug(f"bcm = {bcm}")
        utils.relay_call(bcm, 1)
        rv = {"zoneOff": f"{zone}", "timestamp": f"{timestamp}"}
        logger.info(f"rv = {rv}")
        return Response(rv)


class DeleteSchedule(APIView):
    """Delete a schedule"""

    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def delete(request, zs_id):
        utils.delete_crontab_entry(zs_id)
        rv = {"delete_id": f"{zs_id}"}
        logger.info(f"rv = {rv}")
        return Response(rv)


class ListJobs(APIView):
    """List Schedule details"""

    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        zone_list = ZoneMap.objects.order_by("num")
        job_list = list()
        for zone in zone_list:
            schedule = ZoneSchedule.objects.filter(zone__exact=zone.num).order_by("dow")
            if len(schedule) > 0:
                zs_list = list()
                for s in schedule:
                    zs_dict = dict()
                    zs_dict["dow"] = utils.dow_to_day(s.dow)
                    zs_dict["start"] = s.start.isoformat(timespec="minutes")
                    zs_dict["end"] = s.end.isoformat(timespec="minutes")
                    # zs_dict['active'] = s.active
                    zs_list.append(zs_dict)
                job_dict = dict()
                job_dict[zone.num] = zs_list
                job_list.append(job_dict)

        return Response(job_list)


class Running(APIView):
    """Check what is currently running"""

    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        return Response(utils.whats_running())
