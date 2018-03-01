# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json


from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from forms import *
from models import *

User = get_user_model()
# routes do RENDER

@login_required(login_url='/')
def index(request):
    return render(request, 'dashboard_app/index.html')

@login_required(login_url='/')
def get_wishlist(request):
    arr = []
    snapshot = Snapshot.objects.filter(user_id = request.user.id)
    for snap in snapshot:
        g_id = snap.glasses_id
        arr.append(g_id)
    glasses = Glasses.objects.using('glasses').filter(id__in=arr)
    snap = Snapshot.objects.filter(user_id=request.user.id)
    for s in snap:
        print s

    user_glasses = {
        'glasses': glasses,
        'route': Snapshot.objects.filter(user_id=request.user.id)
    }
    return render(request, 'dashboard_app/wishlist.html', user_glasses)

@login_required(login_url='/')
def webcam(request):
    glasses = {
        'glasses': Glasses.objects.using('glasses').all(),
    }
    return render(request, 'dashboard_app/webcam.html', glasses)

# routes don't render

@csrf_exempt
@login_required(login_url='/')
def wishlist_process(request):
    id = request.POST.get('glasses_id')
    # below checks if this glasses id exists
    print id
    try:
        g = Glasses.objects.using('glasses').get(id=int(id))
    except:
        return HttpResponse(status=400)
    # if exists, we will save the id to the wishlist json string
    wishlist = json.loads(request.user.wishlist)
    if not g.id in wishlist:
        wishlist.append(g.id)
    request.user.wishlist = json.dumps(wishlist)
    request.user.save()
    return HttpResponse('saved to wishlist')

@csrf_exempt
@login_required(login_url='/')
def get_glasses(request):
    dict = {}
    glasses = Glasses.objects.using('glasses').all()
    for g in glasses:
        dict[g.id] = g.route
    return JsonResponse(dict)

@login_required(login_url='/')
def process(request, id):
    g = Glasses.objects.using('glasses').get(id=id)
    request.session['g_route'] = g.route
    return redirect('/dashboard/webcam')

@csrf_exempt
@login_required(login_url='/')
def save_snapshot(request):
    if request.method == 'POST':
        form = UploadSnapshotForm(request.POST, request.FILES)
        if form.is_valid():
            imagefile = Snapshot.objects.create(
                file_upload = form.cleaned_data.get('file'),
                user = request.user, glasses_id = request.POST['glasses_id']
            )
            return HttpResponse('file uploaded')
        else:
            print form.errors
    return HttpResponse('failed')

@login_required(login_url='/')
def find_store(request):
    return render(request, 'dashboard_app/findstore.html')

def delete(request, id):
    Snapshot.objects.get(id=id).delete()
    return redirect('/dashboard/wishlist')
