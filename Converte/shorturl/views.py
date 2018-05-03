# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import requests
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import redis
import re
# Create your views here.

from models import shortUrl

list62 = ['z', 'm', 'x', 'n', 'c', 'v', 'g', 'f', 'h', 'd', 'j', 's', 'k', 'a', 'l', 'q', 'p', 'w', 'o', 'e', 'i', 'r',
          'u', 't', 'y', 'b', 'A', 'S', 'X', 'Z', 'Q', 'W', 'E', 'R', 'D', 'F', 'C', 'V', 'T', 'Y', 'G', 'H', 'B', 'N',
          'M', 'J', 'K', 'L', 'U', 'I', 'O', 'P', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
redis_con = redis.Redis(host='127.0.0.1', port=6379)


@api_view(['POST'])
def generateShortUrlId(request):
    data = request.data
    Url = data['url']
    redisExist = redis_con.get(Url)
    if redisExist:
        text = 'domain' + redisExist
        return Response(text, status=status.HTTP_200_OK)
    else:
        try:
            limit = data['limit']
        except:
            limit = -1
        try:
            title = data['title']
        except:
            title = ''
        if re.search(re.compile('http://'), Url):
            header = 'http://'
            Url = Url.replace('http://', '')
        elif re.search(re.compile('https://'), Url):
            header = 'https://'
            Url = Url.replace('https://', '')
        else:
            header = 'http://'
        newUrl = shortUrl()
        newUrl.url = Url
        newUrl.limitCount = limit
        newUrl.header = header
        newUrl.title = title
        newUrl.save()
        shortCode = encode(newUrl.id)
        if title != '':
            redis_con.setex(Url, title, 3600)
            text = 'domain' + title
        else:
            redis_con.setex(Url, shortCode, 3600)
            text = 'domain' + shortCode
        return Response(text, status=status.HTTP_200_OK)


@api_view(['POST'])
def checkTitle(request):
    data = request.data
    title = data['title']
    try:
        titleExist = shortUrl.objects.get(title=title)
        return Response({'status':'error','msg':u'该title已存在'},status=status.HTTP_200_OK)
    except Exception,e:
        if e.message == 'shortUrl matching query does not exist.':
            return Response({'status': 'ok', 'msg': u'该title可以使用'}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'msg': u'该title不允许使用'}, status=status.HTTP_200_OK)


def encode(id, alphabet=list62):
    """Encode a positive number in Base X

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    if id == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while id and len(arr) <= 7:
        id, rem = divmod(id, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)
