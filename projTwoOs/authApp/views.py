# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib import messages

from django.contrib.auth import login as ulogin, logout as ulogout, authenticate
from forms import *

# Create your views here.

def login_page(request):
    return render(request, 'authApp/login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'authApp/register.html', context={
            'regform': RegistrationForm(),
        })
    elif request.method == 'POST':
        regform = RegistrationForm(request.POST)
        if not regform.is_valid():
            return render(request, 'authApp/register.html', context={
                'regform': regform,
            })
        # form valid
        user = regform.save() # registration succeeded
        ulogin(request, user) # user logged in
    return redirect('/')

def login(request):
    if request.method == 'GET':
        return render(request, 'authApp/login.html')        
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            ulogin(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, 'failed to login')
            return redirect('/')

def logout(request):
    ulogout(request)
    return redirect('/')