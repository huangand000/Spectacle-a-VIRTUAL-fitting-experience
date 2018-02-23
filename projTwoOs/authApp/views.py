# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib import messages

from forms import *

# Create your views here.

def register_page(request):
    return render(request, 'register.html', context={
        'regform': RegistrationForm(),
    })


def register(request):
    if request.method == 'POST':
        regform = RegistrationForm(request.POST)
        if not regform.is_valid():
            print regform.errors
            messages.warning(request, regform.errors) 
            return redirect('/auth/register')
        print 'success'
        user = regform.save()
        return redirect('/')