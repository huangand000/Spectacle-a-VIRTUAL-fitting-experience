# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from twitter import *

# Create your views here.

def twitter(request):

    t = Twitter(
        auth=OAuth('2990475133-m93dLsG6UoGtzm6aHSq89xmX1Z2Ysa8anGuCPU5', 'hk1cMw7EqwAVANozQNjMRVgqacoiGGQ2FVTaHmvsJjTuU', 'bnqpiVEnkqnOlfQFbxJHBJjoM', 'lcODwzLhRZV4OgHFxlaZphdT5IQGbas64ZsSiTCwbbpflazcJW')
        )

    tweets = t.search.tweets(q='#glasses trend', result_type='mixed', lang='en',include_entities='false')

    dictFinal = []
    for items in range(0,len(tweets['statuses'])):
        dictInter = []
        twits=(tweets['statuses'][items]['text'].split('http')[0])
        url=(tweets['statuses'][items]['text'].split('http')[1].split('s://')[1])
        dictInter.append(twits)
        dictInter.append(url)
        dictFinal.append(dictInter)
        dictInter = []

    context = {
        'data':dictFinal
        }     

    return render(request,'twits/index.html',context)


