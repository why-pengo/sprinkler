from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
from loguru import logger
from controller import utils


class HomeView(View):

    @staticmethod
    @login_required()
    def get(request):
        logger.debug("entering...")
        running = utils.whats_running()
        return render(request, 'index.html', {'zones': range(1, 6)})

