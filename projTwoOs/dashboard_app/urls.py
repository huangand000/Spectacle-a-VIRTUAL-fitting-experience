from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^wishlist/$', views.get_wishlist),
    url(r'^wishlist_process/$', views.wishlist_process),
    url(r'^webcam/$', views.webcam),
    url(r'^process/(?P<id>\d+)$', views.process),
    url(r'^save_snapshot$', views.save_snapshot),
    url(r'^get_glasses/', views.get_glasses),
    url(r'^find_store/', views.find_store),
    url(r'^delete/(?P<id>\d+)', views.delete),


]