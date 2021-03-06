#coding:utf-8
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from models import UserProfile
from .forms import LoginForm, RegisterForm

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):

        try:
            user = UserProfile.objects.get(Q(username = username) | Q(email = username)) # "|" 或 "," 和
            if user.check_password(raw_password = password): # 传入明文密码加密后跟数据库中的密码对比
                return user
        except Exception as e:
            return None

# 基于类处理
class LoginView(View):

    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "index.html", {"msg":u"用户名或密码错误"})

        else:
            return render(request, "login.html", {"login_form": login_form})

# 基于方法处理
# def user_login(request):
#     if request.method == "POST":
#         user_name = request.POST.get("username", "")
#         pass_word = request.POST.get("password", "")
#         user = authenticate(username = user_name, password = pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html", {"msg":u"用户名或密码错误!"})
#
#     elif request.method == "GET":
#         return render(request, "login.html", {})


class Registerview(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})

    def post(selfs, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()

            user_profile.username = user_name
            user_profile.password = user_name

            user_profile.password = make_password(pass_word)

            user_profile.save()