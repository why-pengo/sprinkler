from rest_framework import viewsets
from .models import ZoneMap, ZoneSchedule
from .serializers import ZoneMapSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from loguru import logger
from .forms import SchedulerForm
from controller import utils


class ZoneMapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ZoneMap to be viewed or edited.
    """
    queryset = ZoneMap.objects.all().order_by('num')
    serializer_class = ZoneMapSerializer


class ScheduleView(View):
    form_class = SchedulerForm
    template_name = 'schedule.html'

    def get(self, request, zs_id):
        dow = str()
        start = str()
        end = str()
        active = True
        run_once = False
        zone = str()
        if zs_id == '0':
            initial = {
                'zone': 'New'
            }
            form = self.form_class(initial=initial)
        else:
            # zone_obj = ZoneSchedule.objects.get(zone__exact=zone)
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
            form = self.form_class()
        return render(request, self.template_name, {
            'form': form,
            'id': zs_id,
            'dow': dow,
            'start': start,
            'end': end,
            'active': active,
            'run_once': run_once,
            'zone': zone,
        })

    def post(self, request):
        form = self.form_class(request.POST)
        logger.debug(request.POST)
        sub_type = str()
        if 'sub_type' in request.POST:
            sub_type = request.POST['sub_type']
        logger.debug(f"sub_type = {sub_type}")
        if form.is_valid():
            logger.debug(f"is_valid")
            if sub_type == 'Save':
                dow = request.POST['dow']
                start = request.POST['start']
                end = request.POST['end']
                zone = request.POST['zone']
                active = request.POST['active']
                # run_once = request.POST['run_once']
                logger.debug(f"dow = {dow}")
                logger.debug(f"start = {start}")
                logger.debug(f"end = {end}")
                logger.debug(f"zone = {zone}")
                logger.debug(f"active = {active}")
                # logger.debug(f"run_once = {run_once}")
                zone_obj = ZoneSchedule()
                zone_obj.dow = dow
                zone_obj.start = start
                zone_obj.end = end
                zone_obj.zone = zone
                zone_obj.active = True if active == 'on' else False
                # zone_obj.run_once = True if run_once == 'on' else False
                zone_obj.save()
                utils.save_crontab_entry(str(zone_obj.id))
            if sub_type == 'Delete':
                zs_id = request.POST['zs_id']
                utils.delete_crontab_entry(zs_id)
            return HttpResponseRedirect('/schedules')
        else:
            logger.debug(f"{form.errors}")

        return render(request, self.template_name, {'form': form})


class SchedulesView(View):
    template_name = 'schedules.html'

    def get(self, request):
        schedules = ZoneSchedule.objects.all()
        return render(request, self.template_name, {'schedules': schedules})

