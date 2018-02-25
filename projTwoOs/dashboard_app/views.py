# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    return render(request, 'dashboard_app/index.html')

@login_required()
def wishlist(request):
    return render(request, 'dashboard_app/wishlist.html')

@login_required()
def webcam(request):
    return render(request, 'dashboard_app/webcam.html')

@login_required()
def process(request):
    request.session['image'] = request.POST['data']
    print request.session['image']
    return redirect('/dashboard/webcam')