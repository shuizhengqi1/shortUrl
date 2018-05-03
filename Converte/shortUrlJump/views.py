# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from shorturl.models import shortUrl
from shorturl.models import urlVisit
from rest_framework.decorators import api_view
list62 = ['z','m','x','n','c','v','g','f','h','d','j','s','k','a','l','q','p','w','o','e','i','r','u','t','y','b','A','S','X','Z','Q','W','E','R','D','F','C','V','T','Y','G','H','B','N','M','J','K','L','U','I','O','P','0','1','2','3','4','5','6','7','8','9']

def decode(shortID,alphabet=list62):
    base = len(alphabet)
    strlen = len(shortID)
    num = 0

    idx = 0
    for char in shortID:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1
    return num

@api_view(['GET'])
def getUrl(request,shortId):
    if shortId != 'favicon.ico':
        titleExist = shortUrl.objects.filter(title=shortId).all()
        if titleExist.count():
            id = titleExist[0].id
        else:
            id = decode(shortId)
        result = shortUrl.objects.get(id=id)
        if result.limitCount != -1 and result.visitCount >= result.limitCount:
            return HttpResponse('对不起，页面已达限制次数，不能打开')
        else:
            result.visitCount = result.visitCount+1
            result.save()
            url = result.header+result.url
            urlVisit.objects.create(url=url,ip=request.META['REMOTE_ADDR'],headers=request.META['HTTP_USER_AGENT'])
            print url
            return HttpResponseRedirect(url)
    else:
        return Response('',status=status.HTTP_200_OK)
