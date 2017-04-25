#coding:utf-8
from random import Random
from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from mxonline.settings import EMAIL_FROM

def random_str(randomlength = 8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    mRandom = Random()
    for i in range(randomlength):
        str += chars[mRandom.randint(0, length)]
    return str

def send_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_title = u""
    email_body = u""
    if send_type == "register":
        email_title = u"注册激活链接"
        email_body = u"请点击下面的链接激活您注册的账号：http://127.0.0.1/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

        if send_status:
            pass