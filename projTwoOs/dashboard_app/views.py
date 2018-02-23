# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'dashboard_app/index.html')

def wishlist(request):
    return render(request, 'dashboard_app/wishlist.html')

def webcam(request):
    return render(request, 'dashboard_app/webcam.html')

def process(request):
    request.session['image'] = request.POST['data']
    print request.session['image']
    return redirect('/dashboard/webcam')