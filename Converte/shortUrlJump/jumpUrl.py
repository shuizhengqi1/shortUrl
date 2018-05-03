# -*- coding:utf-8 -*-  
# author = yang heng xing
# email =shuizhengqi1@163.com
# date = 2018/1/3 下午9:31
# filename=jumpUrl
from django.conf.urls import url
from views import getUrl

urlpatterns = [
    url(r'^(.*)$',getUrl),
]
