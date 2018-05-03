# -*- coding:utf-8 -*-  
# author = yang heng xing
# email =shuizhengqi1@163.com
# date = 2017/12/11 下午10:48
# filename=shortUrl_setting
from django.utils.crypto import get_random_string

from Converte.settings import *


SITE_ID = 1

ROOT_URLCONF = 'shorturl.shortUrl_url'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'shorturl'
    # other apps specific to this domain
)
