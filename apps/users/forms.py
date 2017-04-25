#coding:utf-8

from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):

    username = forms.CharField(required = True) # 必须有
    password = forms.CharField(required = True, min_length = 6) #减少查询

class RegisterForm(forms.Form):

    email = forms.EmailField(required = True)
    password = forms.CharField(required = True, min_length = 8)
    captcha = CaptchaField(error_messages = {"invalid":u"验证码错误"})