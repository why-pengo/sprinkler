from rest_framework import viewsets
from .models import ZoneMap, ZoneSchedule
from .serializers import ZoneMapSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from loguru import logger
from controller import utils


class ZoneMapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ZoneMap to be viewed or edited.
    """

    queryset = ZoneMap.objects.all().order_by("num")
    serializer_class = ZoneMapSerializer


class ScheduleView(View):
    template_name = "schedule.html"

    def get(self, request, zs_id):
        dow = str()
        start = str()
        end = str()
        active = True
        run_once = False
        zone = str()
        crontab = str()
        cron_key = str()
        zone_obj = ZoneSchedule.objects.get(pk=zs_id)
        logger.debug(f"id = {zs_id}")
        logger.debug(f"zone = {zone_obj.zone}")
        logger.debug(f"dow = {zone_obj.dow}")
        dow = zone_obj.dow
        start = zone_obj.start
        end = zone_obj.end
        active = zone_obj.active
        run_once = zone_obj.run_once
        zone = zone_obj.zone
        crontab = zone_obj.crontab
        cron_key = zone_obj.cron_key
        return render(
            request,
            self.template_name,
            {
                "id": zs_id,
                "dow": dow,
                "start": start,
                "end": end,
                "active": active,
                "run_once": run_once,
                "zone": zone,
                "crontab": crontab,
                "cron_key": cron_key,
            },
        )

    def post(self, request):
        logger.debug(request.POST)
        sub_type = request.POST["sub_type"]
        logger.debug(f"sub_type = {sub_type}")
        if sub_type == "Save":
            dow = request.POST["dow"]
            start = request.POST["start"]
            start = self.convert_to_24_hour(start)
            end = request.POST["end"]
            end = self.convert_to_24_hour(end)
            zone = request.POST["zone"]
            logger.debug(f"dow = {dow}")
            logger.debug(f"start = {start}")
            logger.debug(f"end = {end}")
            logger.debug(f"zone = {zone}")
            zone_obj = ZoneSchedule()
            zone_obj.dow = dow
            zone_obj.start = start
            zone_obj.end = end
            zone_obj.zone = zone
            zone_obj.active = True
            zone_obj.save()
            utils.save_crontab_entry(str(zone_obj.id))
        return HttpResponseRedirect("/schedules")

    @staticmethod
    def convert_to_24_hour(value):
        hm, ampm = value.split(" ", 2)
        hour, minute = hm.split(":", 2)
        if ampm == "PM":
            hour += 12

        return f"{hour}:{minute}"


class SchedulesView(View):
    template_name = "schedules.html"

    def get(self, request):
        schedules_qs = ZoneSchedule.objects.all().order_by("dow")
        schedules = []
        for sch in schedules_qs:
            schedule = {
                "id": sch.id,
                "dow": sch.dow,
                "dow_name": utils.dow_to_day(sch.dow),
                "start": sch.start,
                "end": sch.end,
                "zone": sch.zone,
                "active": sch.active,
                "run_once": sch.run_once,
            }
            schedules.append(schedule)

        return render(request, self.template_name, {"schedules": schedules})
