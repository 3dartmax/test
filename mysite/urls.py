"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test1/', include('test1.urls')),
    url(r'^test2/', include('test2.urls')),
    url(r'^test3/', include('test3.urls')),
    url(r'^testupload/', include('testupload.urls')),
    url(r'^testmiddleware/', include('testmiddleware.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^testmodelform/', include('testmodelform.urls')),
    url(r'^testview/', include('testview.urls')),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
