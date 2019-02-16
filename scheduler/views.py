from django.views import View
from django.shortcuts import render


class HomeView(View):

    @staticmethod
    def get(request):
        render(request, 'index.html')
