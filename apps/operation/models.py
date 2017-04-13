#coding:utf-8

from datetime import datetime

from django.db import models
from users.models import UserProfile
from courses.models import Course
# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length = 20, verbose_name = u"姓名")
    mobile = models.CharField(max_length = 11, verbose_name = u"手机")
    course_name = models.CharField(max_length = 50, verbose_name = u"课程名")
    add_time = models.DateTimeField(default = datetime.now, verbose_name = u'添加时间')

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name = u"用户名")
    course = models.ForeignKey(Course, verbose_name = u"课程名")
    comments = models.CharField(max_length = 200, verbose_name = u"评论")
    add_time = models.DateTimeField(default = datetime.now, verbose_name = u"添加时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name = u"用户")
    # ID 是课程的ID或者是讲师、课程机构的ID
    fav_id = models.IntegerField(default = 0, verbose_name= u"收藏数据ID")
    fav_type = models.IntegerField(choices = ((1, u"课程"), (2, u"课程机构"), (3, u"讲师")), default = 1, verbose_name = u"收藏类型")
    add_time = models.DateTimeField(default = datetime.now, verbose_name = u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

        # 初始化判断是否收藏
        # has_fav = False
        # if request.user.is_authenticated():
        #     if UserProfile.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
        #         has_fav = True


class UserMessage(models.Model):
    # 如果 为 0 代表全局消息，否则就是用户的 ID
    recv_user = models.IntegerField(default = 0, verbose_name = u'接收用户')
    message = models.CharField(max_length = 500, verbose_name = u'消息内容')
    has_read = models.BooleanField(default = False, verbose_name = u'是否已读')
    add_time = models.DateTimeField(default = datetime.now, verbose_name = u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name

# CourseComments 和 UserCourse 字段差不多，可以使用 UserCourse 继承 CourseComments
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name = u'用户')
    course = models.ForeignKey(Course, verbose_name = u'课程')
    add_time = models.DateTimeField(default = datetime.now, verbose_name = u'添加时间')

    class Meta:
        verbose_name = u'用户学习过的课程'
        verbose_name_plural = verbose_name