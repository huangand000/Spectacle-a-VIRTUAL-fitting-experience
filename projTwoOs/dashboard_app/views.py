# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from authApp.models import User
from .models import Glasses
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'dashboard_app/index.html')

def wishlist(request):
    return render(request, 'dashboard_app/wishlist.html')

def webcam(request):
    glasses = {
        'glasses': Glasses.objects.all()
    }
    return render(request, 'dashboard_app/webcam.html', glasses)

def process(request, id):
    g = Glasses.objects.get(id=id)
    request.session['g_route'] = g.route
    return redirect('/dashboard/webcam')