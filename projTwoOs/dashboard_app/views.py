# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from forms import *
from models import *

from image_handler import save_image

User = get_user_model()
# routes do RENDER

@login_required()
def index(request):
    return render(request, 'dashboard_app/index.html')

@login_required()
def wishlist(request):
    u = User.objects.get(id=request.user.id)
    user_glasses = {
        'glasses': u.glasses.all()
    }
    return render(request, 'dashboard_app/wishlist.html', user_glasses)

@login_required()
def webcam(request):
    glasses = {
        'glasses': Glasses.objects.all()
    }
    return render(request, 'dashboard_app/webcam.html', glasses)

# routes don't render

@csrf_exempt
@login_required()
def wishlist_process(request):
    route = request.POST.get('route')
    g = Glasses.objects.get(route=route)
    g.users.add(request.user)
    g.save()
    print g.name
    return HttpResponse('')

@csrf_exempt
@login_required()
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

@csrf_exempt
@login_required()
def save_snapshot(request):
    if request.method == 'POST':
        form = UploadSnapshotForm(request.POST, request.FILES)
        if form.is_valid():
            imagefile = Snapshot.objects.create(
                file_upload = form.cleaned_data.get('file'),
                user = request.user
            )
            return HttpResponse('file uploaded')
        else:
            print form.errors
    return HttpResponse('failed')

