from rest_framework import viewsets
from .models import ZoneMap, ZoneSchedule
from .serializers import ZoneMapSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import SchedulerForm

LP = "scheduler.views::"


class ZoneMapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ZoneMap to be viewed or edited.
    """
    queryset = ZoneMap.objects.all().order_by('num')
    serializer_class = ZoneMapSerializer


class ScheduleView(View):
    form_class = SchedulerForm
    template_name = 'schedule.html'
    lp = f"{LP}ScheduleView:"

    def get(self, request):
        if 'zone' in request.POST:
            zone = request.POST['zone']
        else:
            zone = 'New'

        if zone == 'New':
            initial = {
                'zone': 'New'
            }
            form = self.form_class(initial=initial)
        else:
            zone_obj = ZoneSchedule.objects.get(zone__exact=zone)
            print(f"{self.lp}get:39 zone = {zone}")
            print(f"{self.lp}get:40 dow = {zone_obj.dow}")
            initial = {
                'dow': zone_obj.dow,
                'start': zone_obj.start,
                'end': zone_obj.end,
                'active': zone_obj.active,
                'zone': zone_obj.zone,
            }
            form = self.form_class(initial=initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        zone = request.POST['zone']
        dow = request.POST['dow']
        start = request.POST['start']
        end = request.POST['end']
        zone = request.POST['zone']
        active = request.POST['active']
        print(f"{self.lp}post:59 dow = {dow}")
        print(f"{self.lp}post:60 start = {start}")
        print(f"{self.lp}post:61 end = {end}")
        print(f"{self.lp}post:62 zone = {zone}")
        print(f"{self.lp}post:63 active = {active}")
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


class SchedulesView(View):
    template_name = 'schedules.html'

    def get(self, request):
        schedules = ZoneSchedule.objects.all()
        return render(request, self.template_name, {'schedules': schedules})

