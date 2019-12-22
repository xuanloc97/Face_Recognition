from django.conf.urls import url

from . import views

urlpatterns = [
            url('', views.index, name='index'),
            url('', views.simple_upload, name='simple_load'),
            url('', views.video_feed, name='video_feed'),
        ]