"""photoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from blog import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'), #글 목록
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'), #글 내용
    #url(r'^(?P<pk>[0-9]+)/$', views.post_detail),

    url(r'^(?P<pk>\d+)/comments/new/$', views.comment_new, name='comment_new'), #새 뎃글 쓰기
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'), #뎃글 수정

    url(r'^new/$', views.post_new, name='post_new'),#새 글
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#업로드 된 그림 url지원
