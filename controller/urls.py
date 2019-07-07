from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from status.views import HomeView
from controller.api import ZoneOn, ZoneOff, Running, ListJobs
from scheduler.views import ZoneMapViewSet, SchedulesView, ScheduleView
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r'zones', ZoneMapViewSet)

urlpatterns = [
    # Django
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # sprinkler
    path('', HomeView.as_view()),
    path('schedules', login_required(SchedulesView.as_view())),
    path('schedule', login_required(ScheduleView.as_view())),
    path('schedule/<zs_id>', login_required(ScheduleView.as_view())),

    # api
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('zone_on/<zone>', ZoneOn.as_view()),
    path('zone_off/<zone>', ZoneOff.as_view()),
    path('running/', Running.as_view()),
    path('list_jobs/', ListJobs.as_view()),
]

