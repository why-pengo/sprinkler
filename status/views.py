from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
from loguru import logger


class HomeView(View):

    @staticmethod
    @login_required()
    def get(request):
        logger.debug("entering...")
        return render(request, 'index.html', None)


# class LoginView(View):
#
#     @staticmethod
#     def post(request):
#         print(f"scheduler/views::post: entering.")
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             print(f"scheduler/views::post: user authenticated.")
#             login(request, user)
#             # redirect
#             return redirect(request.GET.get('next'))
#         else:
#             print(f"scheduler/views::post: user not authenticated.")
#             # Return an 'invalid login' error message.
#             pass
