from django.conf.urls import url
from . import views

app_name = 'testupload'

urlpatterns = [
    url(r'^$', views.UploadList, name='list'),
    url(r'^(?P<pk>[0-9]+)/view/$', views.UploadView, name='view'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.UploadDetail, name='detail'),
]
