# -*- coding:utf-8 -*-  
# author = yang heng xing
# email =shuizhengqi1@163.com
# date = 2018/1/3 下午9:42
# filename=jump_setting
from django.utils.crypto import get_random_string

from Converte.settings import *


SITE_ID = 1

ROOT_URLCONF = 'shortUrlJump.jumpUrl'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'shortUrlJump',
    'shorturl'
    # other apps specific to this domain
)


