from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^bot$', views.bot),
    url(r'^twitter$', views.twitter)

]