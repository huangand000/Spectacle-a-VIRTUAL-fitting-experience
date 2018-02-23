# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'dashboard_app/index.html')

def wishlist(request):
    return render(request, 'dashboard_app/wishlist.html')