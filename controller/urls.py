from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from status.views import HomeView

urlpatterns = [
    # Django
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', LoginView.as_view(template_name='accounts/login.html')),

    # sprinkler
    path('', login_required(HomeView.as_view())),
]
