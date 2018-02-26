from django.conf.urls import url

from django.shortcuts import redirect

from . import views

urlpatterns = [
    url(r'^$', lambda req: redirect('/auth/login')),

    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),

]