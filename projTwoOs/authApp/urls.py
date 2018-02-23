from django.conf.urls import url

from django.shortcuts import redirect

from . import views

urlpatterns = [
    url(r'^$', lambda req: redirect('/auth/register')),

    # routes that render htmls
    url(r'^register$', views.register_page),

    # routes that don't render htmls
    url(r'^user/create$', views.register),
]