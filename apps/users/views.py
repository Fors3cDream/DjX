from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from models import UserProfile

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):

        try:
            user = UserProfile.objects.get(Q(username = username) | Q(email = username))
            if user.check_password(raw_password = password):
                return user
        except Exception as e:
            return None


def _login(request):
    if request.method == "GET":
        return render(request, "login.html", {})
    elif request.method == "POST":
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username = user_name, passwowrd = pass_word)
        if user is not None:
            login(request, user)
            return render(request, "index.html", {})
        else:
            return render(request, "login.html", {})