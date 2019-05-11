from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from status.views import HomeView
from controller.api import ZoneOn, ZoneOff, Running, ListJobs
from scheduler.views import ZoneMapViewSet

router = routers.DefaultRouter()
router.register(r'zones', ZoneMapViewSet)

urlpatterns = [
    # Django
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # sprinkler
    path('', HomeView.as_view()),

    # api
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-auth/zone_on/', ZoneOn.as_view()),
    path('api-auth/zone_off/', ZoneOff.as_view()),
    path('api-auth/running/', Running.as_view()),
    path('api-auth/list_jobs/', ListJobs.as_view()),
]
