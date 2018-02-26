from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^wishlist/$', views.wishlist),
    url(r'^webcam/$', views.webcam),
    url(r'^process/(?P<id>\d+)$', views.process),
    url(r'^save_process/', views.save_process)
]