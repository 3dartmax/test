from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/post_detail.html/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_pk>\d+)/comment/new/$', views.comment_new, name='comment_new')
]