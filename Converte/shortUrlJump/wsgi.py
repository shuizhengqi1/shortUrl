# -*- coding:utf-8 -*-  
# author = yang heng xing
# email =shuizhengqi1@163.com
# date = 2018/1/3 下午9:42
# filename=jump_wsgi

import os
import sys

import django
from django.core.wsgi import get_wsgi_application

# Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'shortUrlJump.jump_setting'

sys.stdout = sys.stderr

application = get_wsgi_application()

django.setup()