"""projTwoOs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import redirect
import dashboard_app
import os

def index_redirect(request):
    if request.user.is_authenticated:
        return redirect('/auth')
    else:
        return redirect('/dashboard')

urlpatterns = [
    url(r'^$', lambda req: redirect('/auth')),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('authApp.urls')),
    url(r'^dashboard/', include('dashboard_app.urls')),
    url(r'^chatbot/', include('chatbot.urls')),
] + static('snap/', document_root=(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))))

