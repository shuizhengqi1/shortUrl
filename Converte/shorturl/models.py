# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class shortUrl(models.Model):
    url = models.TextField(u'原始url')
    header = models.CharField(u'头部信息',max_length=20,default='http://')
    limitCount = models.IntegerField(u'限制次数',default=-1)
    visitCount = models.IntegerField(u'访问次数',default=0)
    title = models.CharField(u'自定义标题',max_length=20,default='')
    visitTime = models.DateTimeField(auto_now=True)


class urlVisit(models.Model):
    url = models.TextField(u'url')
    ip = models.TextField(u'ip')
    headers = models.TextField(u'头部信息')
    visitTime = models.DateTimeField(auto_now=True)

class userInfo(models.Model):
    openId = models.CharField(u'用户openId',max_length=255)
    number = models.CharField(u'手机号码',max_length=20)
    updateTime = models.DateTimeField(auto_now_add=True)
