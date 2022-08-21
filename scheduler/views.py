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

    def get(self, request):
        dow = str()
        start = str()
        end = str()
        active = True
        run_once = False
        zone = str()
        crontab = str()
        cron_key = str()
        return render(
            request,
            self.template_name,
            {
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
            if dow.find(",") != -1:
                dows = dow.split(",")
                logger.debug(f"dows = {dows}")
                for i in dows:
                    zone_obj = ZoneSchedule()
                    zone_obj.dow = i
                    zone_obj.start = start
                    zone_obj.end = end
                    zone_obj.zone = zone
                    zone_obj.active = True
                    zone_obj.save()
                    utils.save_crontab_entry(str(zone_obj.id))
            else:
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
