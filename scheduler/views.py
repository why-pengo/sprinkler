from rest_framework import viewsets
from .models import ZoneMap
from .serializers import ZoneMapSerializer
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import SchedulerForm
from .models import ZoneSchedule


class ZoneMapViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ZoneMap to be viewed or edited.
    """
    queryset = ZoneMap.objects.all().order_by('num')
    serializer_class = ZoneMapSerializer


class ScheduleView(View):
    form_class = SchedulerForm
    initial = {'key': 'value'}
    template_name = 'schedule.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class SchedulesView(View):
    template_name = 'schedules.html'

    def get(self, request):
        schedules = ZoneSchedule.objects.all()
        return render(request, self.template_name, {'schedules': schedules})

