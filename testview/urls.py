from django.conf.urls import url
from . import views

app_name = 'testview'

urlpatterns = [
    # 방법1-1.
    #url(r'^about/$', views.my_view),
    # 방법1-2.
    url(r'^about/$', views.MyView.as_view(greeting='3dartmax에 오신걸 환영합니다.')),

    url(r'^vote/$', views.MyFormView.as_view()),
    url(r'^success/$', views.MySuccessView.as_view()),
]