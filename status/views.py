from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from loguru import logger


class HomeView(View):
    @staticmethod
    @login_required()
    def get(request):
        logger.debug("entering...")
        return render(request, "index.html", {"zones": range(1, 6)})
