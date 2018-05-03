# -*- coding:utf-8 -*-  
# author = yang heng xing
# email =shuizhengqi1@163.com
# date = 2017/12/11 下午10:51
# filename=url
from django.conf.urls import url
from shorturl.views import generateShortUrlId,checkTitle
urlpatterns = [
    url(r'^shortUrl',generateShortUrlId),
    url(r'^checkTitle',checkTitle)
]
