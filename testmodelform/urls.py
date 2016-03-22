from django.conf.urls import url
from . import views

app_name = 'testmodelform'

urlpatterns = [
    url(r'^author_list.html/$',                 views.author_list,   name='author_list'),
    url(r'^(?P<pk>\d+)/author_detail.html/$', views.author_detail, name='author_detail'),
    url(r'^author/new/$',                        views.author_new,    name='author_new'),

    url(r'^book_list.html/$',                   views.book_list,     name='book_list'),
    url(r'^(?P<pk>\d+)/book_detail.html/$',   views.book_detail,   name='book_detail'),
    url(r'^book/new/$',                          views.book_new,      name='book_new'),
]