# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from authApp.models import User
from .models import Glasses
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from forms import *

from image_handler import save_image

@login_required()
def index(request):
    return render(request, 'dashboard_app/index.html')

@login_required()
def wishlist(request):
    u = User.objects.get(id=request.user.id)
    user_glasses = {
        'glasses': u.glasses.all()
    }

    Snapshot.file_upload.create(file = "", user = User.objecst.get(id=id))
    return render(request, 'dashboard_app/wishlist.html', user_glasses)

@csrf_exempt
def wishlist_process(request):
    route = request.POST.get('route')
    g = Glasses.objects.get(route=route)
    g.users.add(request.user)
    g.save()
    print g.name
    return HttpResponse('')

@login_required()
def webcam(request):
    glasses = {
        'glasses': Glasses.objects.all()
    }
    return render(request, 'dashboard_app/webcam.html', glasses)

@csrf_exempt
def get_glasses(request):
    dict = {}
    glasses = Glasses.objects.all()
    for g in glasses:
        dict[g.id] = g.route
    return JsonResponse(dict)

@login_required()
def process(request, id):
    g = Glasses.objects.get(id=id)
    request.session['g_route'] = g.route
    return redirect('/dashboard/webcam')

@login_required()
def save_process(request):
    if request.method == 'POST':
        print 'arrived'
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print 'a1'
            save_image(request.FILES['file'])# handle file
            return HttpResponse('file uploaded')
        else:
            print form.errors
    return HttpResponse('failed')

