from django.contrib import admin
from django.urls import path, include
from status.views import HomeView

urlpatterns = [
    # Django
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # sprinkler
    path('', HomeView.as_view()),
]
