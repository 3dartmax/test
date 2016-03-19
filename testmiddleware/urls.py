from django.conf.urls import url
from . import views

app_name = 'testmiddleware'

urlpatterns = [
    # 방법1. - Middleware사용하기
    #url(r'^$', views.MiddlewareList, name='list'),

    # 방법2-1. - ListView사용하기
    url(r'^memo_list.html/$', views.PageListView, name='memo_list'),                        # ListView
    # 방법2-2. - DetailView사용하기
    url(r'^(?P<pk>[0-9]+)/memo_detail.html/$', views.PageDetailView, name='memo_detail'), # DetailView
]